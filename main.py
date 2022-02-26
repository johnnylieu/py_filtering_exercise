import csv
import sys
import time

t0 = time.time()
print(t0)

input = sys.argv[1]
output = sys.argv[2]
min_dis = int(sys.argv[3])
max_dis = int(sys.argv[4])

with open(sys.argv[1], 'r') as metafile:
    with open(sys.argv[2], 'x') as output_file: # using x instead of w returns an error if file already exists
        lines = metafile.readlines()
        total_lines = len(lines)
        output_line = 0
        for line in lines:
            elements = line.split(",")
            distance = int(elements[-1])

            if distance >= min_dis and distance <= max_dis:
                output_file.write(line)


t1 = time.time()
print(t1)

total_time = t1 - t0
print(total_time)

# task 2
# # of total rows
# # of rows discarded
# % of pictures within desired range
# total execution time of the filter operation

# task 1
# python main.py path_to_input_csv path_to_output_csv min_dist max_dist