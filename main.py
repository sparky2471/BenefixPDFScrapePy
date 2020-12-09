import os
import tabula
import shutil
import csv

directory = 'Engineering_Test/'
file = 'Engineering_Test/para01.csv'

shutil.copy('BeneFix Small Group Plans upload template.xlsx', 'BeneFix Small Group Plans upload template_copy.xlsx')

tabula.convert_into_by_batch(directory, output_format='csv', pages='all')

for file in os.listdir(directory):
    if file.endswith('.csv'):
        with open(os.path.join(directory, file), 'r') as infile, open(('output.csv', file), 'w', newline='') as outfile:
            csv_reader = csv.reader(infile)
            csv_writer = csv_writer(outfile)
            for line in csv_reader:
                if all(line):
                    csv_writer.writerow(line)


# def parse_csv():
#     with open('Engineering_Test/para01.csv') as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter=',')
#         line_count=0
#         for row in csv_reader:
#             if line_count ==0:
#                 print(f'Column names are {", ".join(row)}')
#                 line_count += 1
#             else:
#                 print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
#                 line_count += 1
#             print(f'Processed {line_count} lines.')
#
#         print(csv_reader)