import csv
from faker import Faker


def anonymize_chunk(input_file, output_file, chunk_size=100_000):
    fake = Faker()
    with open(input_file, 'r', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        header = next(reader)

        with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(header)  # Write header

            batch = []
            for row in reader:
                batch.append([
                    fake.first_name(),  # Anonymized first_name
                    fake.last_name(),   # Anonymized last_name
                    fake.address().replace('\n', ', '),  # Anonymized address
                    row[3]  # Keep date_of_birth unchanged
                ])

                if len(batch) >= chunk_size:
                    writer.writerows(batch)
                    batch = []

            # Write remaining rows
            if batch:
                writer.writerows(batch)


if __name__ == "__main__":
    input_file = 'large_sample.csv'
    output_file = 'anonymized_large_sample.csv'
    anonymize_chunk(input_file, output_file)
    print(f"Data anonymized and saved to {output_file}.")
