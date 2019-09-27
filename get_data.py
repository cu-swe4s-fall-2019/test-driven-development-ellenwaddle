#should take a column number and return an array of numbers that correspond
#to values from stdin at the col number position
import sys

alllines=[]

def read_stdin_col(col_num):

    if col_num < 1:

        return None

    else:

        focal_data = []

        for line in sys.stdin:

            lines = line.rstrip().split()
            alllines.append(lines)
            a = lines[col_num]
            focal_data.append(a)

        return focal_data

print(read_stdin_col(2))
