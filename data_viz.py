#should take a numerical array (from get_data.py) and output plot file name as parameters
#use methods in math_lib to calculate summary statistics
#create plots saved at output file location with mean, sd in the title and axis labeled
import sys
#import get_data
#import math_lib as ml
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pathlib


def boxplot(L, out_file_name):
    file=pathlib.Path(out_file_name)

    if file.exists():
        return ('this file name is taken, choose another.')
    else:
        return ('file does not exist yet')

def histogram(L, out_file_name):
    pass

def combo(L, out_file_name):
    pass
