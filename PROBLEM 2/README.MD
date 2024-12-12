# CSV Anonymizer

This project processes large CSV files to anonymize sensitive fields like `first_name`, `last_name`, and `address`. It is scalable for both small and large datasets, leveraging chunk-based processing on single machines and distributed processing using Apache Spark for massive datasets.

---

## How to Run

### Local Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/csv-anonymizer.git
   cd csv-anonymizer
   ```

## Install Dependencies

pip install -r requirements.txt

## Generate a Sample CSV:

python generate_csv.py
This creates a large_sample.csv file.

##Anonymize the Data:
python anonymize_csv.py
This creates an anonymized_large_sample.csv file.

## Using Docker

Build the Docker Image:
docker build -t csv-anonymizer .
Run the Docker Container:
docker run --rm -v $(pwd):/app csv-anonymizer

## Check Output:

The generated files (large_sample.csv and anonymized_large_sample.csv) will be available in the current directory.
Distributed Processing with Apache Spark

## Start a Spark Cluster:

Install Apache Spark and start the cluster. For local testing, you can use a standalone Spark installation.

## Run the Spark Script:

spark-submit spark_anonymize.py
This processes the file in parallel and creates an anonymized output
