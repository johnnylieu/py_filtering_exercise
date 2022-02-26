import csv
import sys
import time

t0 = time.time()

input = sys.argv[1]
output = sys.argv[2]
min_dis = sys.argv[3]
max_dis = sys.argv[4]

with open(sys.argv[1], 'r') as metafile:
    reader = csv.reader(metafile, delimiter=",")
    for row in reader:
        distance = int(row[-1])
            with open(sys.argv[2], 'x') as output_file: # using x instead of w returns an error if file already exists
                lines = metafile.readlines()
                total_lines = len(lines)
                output_line = 0

                if distance >= min_dis and distance <= max_dis:
                    output_file.write(lines)

t1 = time.time()

total_time = t1 - t0

# task 2
# # of total rows
# # of rows discarded
# % of pictures within desired range
# total execution time of the filter operation

# task 1
# python main.py path_to_input_csv path_to_output_csv min_dist max_dist