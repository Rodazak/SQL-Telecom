import csv
import sys

# Increase the field size limit
csv.field_size_limit(sys.maxsize)
# CSV file details
csv_file = '/home/bruno/python/CEQ_EVENTOS_HFC.csv'
column_index = 4  # Index of the column to compare (0-based index)
values_to_keep = ['CORTINA,GERARDO', 'SOBOL,CARLOS ALBERTO', 'ALVAREZ,LEONEL CARLOS',
                  'BAZAN,ROBERTO GUSTAVO','SANIN,DARIO','OZON,JOSE ANGEL','ORZA,ARIEL','BLANCO LOPEZ,MARCELO']  # List of values to keep

# Read the CSV file and filter rows
rows_to_keep = []
header = None
with open(csv_file, 'r', encoding='ISO-8859-1') as file:
    reader = csv.reader(file,delimiter=';')
    
    for row in reader:
        # Store the header row
        if reader.line_num == 1:
            header = row
            continue

        # Remove newline characters from the row
        cleaned_row = [cell.replace('\n', '') for cell in row]

        # Check if the column value matches any value in the list
        if len(cleaned_row) > column_index and cleaned_row[column_index] in values_to_keep:
            rows_to_keep.append(cleaned_row)

# Write the filtered rows to a new CSV file
output_file = '/home/bruno/python/CEQ_EVENTOS_HFC_B2B.csv'
with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)

    # Write the header row
    if header is not None:
        writer.writerow(header)

    # Write the rows to the new CSV file
    writer.writerows(rows_to_keep)
