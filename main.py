import csv
import sys
import math

output = open(sys.argv[2], 'w')
output_header = "Date, Time, File, x, y, Theta, Distance\n" # optional (not part of task) but looks cleaner
output.write(output_header)

file = open(sys.argv[1])
reader = csv.reader(file)
rowsOriginal = len(list(reader))
print(f"{sys.argv[1]} has {rowsOriginal} rows") #works

minDis = int(sys.argv[3])
maxDis = int(sys.argv[4])
# print(minDis, maxDis) # works

with open(sys.argv[1], 'r') as metafile:
    reader = csv.reader(metafile, delimiter=",")
    # header = next(reader)
    # print(header) # works
    for row in reader:
        date = row[0]
        time = row[1]
        file = row[2]
        x = row[3]
        y = row[4]
        theta = row[5]
        distance = int(row[6])
        # print(row) # works
        line = "{},{},{},{},{},{},{}\n".format(date, time, file, x, y , theta, distance) # output will be in this format for each line
        if distance >= minDis:
            if distance <= maxDis:
                output.write(line) # output of new file will write this line everytime we iterate through a row
output.close()

file = open(sys.argv[2])
reader = csv.reader(file)
rowsNew = len(list(reader))
print(rowsOriginal)
print(rowsNew)
rowsDiscarded = rowsOriginal + rowsNew - 1 # - 1 to account for the header that I added
percent = (rowsNew / rowsOriginal) * 100
# print(percent) #works
print(rowsDiscarded)
print(f"{sys.argv[2]} has {rowsOriginal} rows") #works
print(f"There were {rowsDiscarded} rows discarded")
print(f"There are {percent}% of images within range")
file.close()
metafile.close()

# task 2
# # of total rows
# # of rows discarded
# % of pictures within desired range
# total execution time of the filter operation

# task 1
# python main.py path_to_input_csv path_to_output_csv min_dist max_dist