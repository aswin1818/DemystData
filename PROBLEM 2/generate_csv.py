import csv
import random
from faker import Faker


def generate_csv(file_name, num_rows):
    fake = Faker()
    with open(file_name, 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['first_name', 'last_name',
                        'address', 'date_of_birth'])
        for _ in range(num_rows):
            writer.writerow([
                fake.first_name(),
                fake.last_name(),
                fake.address().replace('\n', ', '),
                fake.date_of_birth()
            ])


if __name__ == "__main__":
    # Generate a sample 2GB file (~20 million rows with approximate size)
    file_name = 'large_sample.csv'
    num_rows = 20_000_000  # Adjust based on testing needs
    generate_csv(file_name, num_rows)
    print(f"{file_name} generated successfully.")
