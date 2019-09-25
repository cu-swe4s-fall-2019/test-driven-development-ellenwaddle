#should take a column number and return an array of numbers that correspond
#to values from stdin at the col number position
import sys

def read_stdin_col(col_num):
    if col_num < 1:
        return None
    for line in sys.stdin:
        line=line.rstrip().split()

    return line
