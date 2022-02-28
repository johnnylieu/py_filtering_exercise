import csv
import sys
import time

t0 = time.time()
# print(t0) # works

input = sys.argv[1]
output = sys.argv[2]
min_dis = int(sys.argv[3])
max_dis = int(sys.argv[4])

with open(input, 'r') as metafile:
    with open(output, 'x') as output_file: # using x instead of w returns an error if file already exists
        lines = metafile.readlines()
        total_lines = len(lines)
        # print(f"total_lines: {total_lines}") # works
        output_line = 0
        for line in lines:
            elements = line.split(",")
            distance = int(elements[-1])

            if distance >= min_dis and distance <= max_dis:
                output_file.write(line)
                output_line += 1
                # print(f"output_line: {output_line}") # works

t1 = time.time()
# print(t1) # works

print(f"\nTask 1 & 2\n\n{input} has a total of {total_lines} rows.\n{output} has a total of {output_line} rows.\nThere were {total_lines - output_line} rows discarded.\n{(output_line / total_lines) * 100}% are within desired range.\nTotal execution time: {t1 - t0}\n\n -Johnny Lieu\n")

def main():
    print("hello world")

if __name__ == "__main__":
    main()

    # def main():
    # beginFilter = Filter(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    # beginFilter.startFilter()
    # filter = Filter("input-path")
    
    # filter.filter_by_distance(min=1,max=2)
    # filter.filter_by_x(min=1,max=2)
    # filter.filter_by_y(min=1,max=2)
    
    # filter.write_file("output-path")