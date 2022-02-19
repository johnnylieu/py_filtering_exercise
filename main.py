import csv
import sys

with open("metadata.csv", 'r') as metafile:
    reader = csv.reader(metafile, delimiter=",")
    header = next(reader)
    print(header)


# python main.py path_to_input_csv path_to_output_csv min_dist max_dist