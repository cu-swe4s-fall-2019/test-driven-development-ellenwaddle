#should take a numerical array (from get_data.py) and output plot file name as parameters
#use methods in math_lib to calculate summary statistics
#create plots saved at output file location with mean, sd in the title and axis labeled
import sys
#import get_data
import math_lib as ml
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pathlib


def histogram(L, out_file_name):
    file=pathlib.Path(out_file_name)

    if file.exists():
        return ('this file name is taken, choose another.')
    else:
        width=3
        height=3
        mean=ml.list_mean(L)
        stdev=ml.list_stdev(L)
        title='mean='+str(mean)+' stdev='+str(stdev)

        fig=plt.figure(figsize=(width,height),dpi=300)

        ax=fig.add_subplot(1,1,1)
        ax.set_title(title)

        ax.hist(L,3)

        plt.savefig(out_file_name,bbox_inches='tight')
        if not file.exists():
            print ('the plot did not save successfully.')



def boxplot(L, out_file_name):
    file=pathlib.Path(out_file_name)

    if file.exists():
        return ('this file name is taken, choose another.')
    else:
        width=3
        height=3
        mean=ml.list_mean(L)
        stdev=ml.list_stdev(L)
        title='mean='+str(mean)+' stdev='+str(stdev)

        fig=plt.figure(figsize=(width,height),dpi=300)
        ax=fig.add_subplot(1,1,1)
        ax.set_title(title)
        ax.boxplot(L)

        plt.savefig(out_file_name,bbox_inches='tight')


        if not file.exists():
            print ('the plot did not save successfully.')


def combo(L, out_file_name):
    file=pathlib.Path(out_file_name)

    if file.exists():
        return ('this file name is taken, choose another.')
    else:
        width=3
        height=3
        mean=ml.list_mean(L)
        stdev=ml.list_stdev(L)
        title='mean='+str(mean)+' stdev='+str(stdev)

        fig=plt.figure(figsize=(width,height),dpi=300)

        ax=fig.add_subplot(2,1,1)
        ax.set_title(title)
        ax.set_ylabel('frequency')
        ax.set_xlabel('value')
        ax.hist(L,3)

        ax2=fig.add_subplot(2,1,2)
        ax2.set_ylabel('frequency')
        ax2.boxplot(L)

        plt.savefig(out_file_name,bbox_inches='tight')

#L=[1,2,2,3,4,5,3]
#histogram(L,'histogram_check.png')
#boxplot(L,'boxplotcheck.png')
#combo(L,'combo')
