import csv
import sys
import timeit

class filter:
    def __init__(self, inputFile, outputFile, min, max):
        self.inputFile = inputFile
        self.outputFile = outputFile
        self.min = min
        self.max = max

    def startFilter(self):
        output = open(self.outputFile, 'w')
        output_header = "Date, Time, File, x, y, Theta, Distance\n" # optional (not part of task) but looks cleaner
        # print(output_header) #works
        output.write(output_header)

        file = open(self.inputFile)
        reader = csv.reader(file)
        rowsOriginal = len(list(reader))

        minDis = int(self.min)
        maxDis = int(self.max)
        # print(rowsOriginal, minDis, maxDis) # works

        with open(self.inputFile, 'r') as metafile:
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
        # print(rowsOriginal) # works
        # print(rowsNew) # works
        rowsDiscarded = rowsOriginal - rowsNew - 1 # - 1 to account for the header that I added
        percent = (rowsNew / rowsOriginal) * 100
        # print(percent) #works
        # print(rowsDiscarded) # works
        print(f"\n{sys.argv[1]} has {rowsOriginal} rows") #works
        print(f"{sys.argv[2]} has {rowsNew} rows") #works
        print(f"There were {rowsDiscarded} rows discarded")
        print(f"There are {percent}% of images within range\n")
        file.close()
        metafile.close()

        print(f"Execution time is: {timeit.timeit()}\n")

def main():
    beginFilter = filter(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    beginFilter.startFilter()

if __name__ == "__main__":
    main()