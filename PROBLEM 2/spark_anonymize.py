from pyspark.sql import SparkSession
from pyspark.sql.functions import lit, udf
from faker import Faker

fake = Faker()


def fake_first_name():
    return fake.first_name()


def fake_last_name():
    return fake.last_name()


def fake_address():
    return fake.address().replace('\n', ', ')


if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("Anonymize CSV Data") \
        .getOrCreate()

    # Define UDFs for anonymization
    fake_first_name_udf = udf(fake_first_name)
    fake_last_name_udf = udf(fake_last_name)
    fake_address_udf = udf(fake_address)

    input_file = "large_sample.csv"
    output_file = "anonymized_large_sample.csv"

    # Read CSV
    df = spark.read.csv(input_file, header=True)

    # Anonymize data
    anonymized_df = df.withColumn("first_name", fake_first_name_udf()) \
                      .withColumn("last_name", fake_last_name_udf()) \
                      .withColumn("address", fake_address_udf())

    # Write anonymized data
    anonymized_df.write.csv(output_file, header=True, mode="overwrite")
    print(f"Anonymized data saved to {output_file}.")
