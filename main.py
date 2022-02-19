import csv
import sys

with open(sys.argv[1], 'r') as metafile:
    reader = csv.reader(metafile, delimiter=",")
    # header = next(reader)
    # print(header) # works
    for row in reader:
        minDis = row[5]
        maxDis = row[6]
        print(minDis, maxDis) # works



# python main.py path_to_input_csv path_to_output_csv min_dist max_dist