import csv
import json


def parse_json_spec_file(spec_file_path):
    """Reads the JSON spec file and extracts column names, offsets, and encoding info."""
    with open(spec_file_path, 'r', encoding='utf-8') as spec_file:
        spec = json.load(spec_file)
    column_names = spec["ColumnNames"]
    offsets = [int(offset) for offset in spec["Offsets"]]
    fixed_width_encoding = spec["FixedWidthEncoding"]
    include_header = spec["IncludeHeader"].lower() == "true"
    delimited_encoding = spec["DelimitedEncoding"]
    return column_names, offsets, fixed_width_encoding, include_header, delimited_encoding


def parse_fixed_width_file(fixed_width_file_path, column_names, offsets, fixed_width_encoding):
    """Parses the fixed-width file based on the offsets and returns rows as lists."""
    rows = []
    with open(fixed_width_file_path, 'r', encoding=fixed_width_encoding) as fixed_width_file:
        for line in fixed_width_file:
            row = []
            start = 0
            for offset in offsets:
                row.append(line[start:start + offset].strip())
                start += offset
            rows.append(row)
    return rows


def write_csv(output_csv_path, column_names, rows, include_header, delimited_encoding):
    """Writes parsed rows to a CSV file."""
    with open(output_csv_path, 'w', encoding=delimited_encoding, newline='') as csv_file:
        writer = csv.writer(csv_file)
        if include_header:
            writer.writerow(column_names)
        writer.writerows(rows)


if __name__ == "__main__":
    # Input paths
    spec_file_path = 'spec_file.json'
    fixed_width_file_path = 'fixed_width_file.txt'
    output_csv_path = 'output.csv'

    # Parse JSON spec file
    (column_names, offsets, fixed_width_encoding,
     include_header, delimited_encoding) = parse_json_spec_file(spec_file_path)

    # Parse fixed-width file
    rows = parse_fixed_width_file(
        fixed_width_file_path, column_names, offsets, fixed_width_encoding)

    # Write CSV file
    write_csv(output_csv_path, column_names, rows,
              include_header, delimited_encoding)

    print(f"CSV file generated at {output_csv_path}")
