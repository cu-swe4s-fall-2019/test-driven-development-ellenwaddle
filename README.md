# test-driven-dev
*Test Driven Development*

`conda install mathplotlib`
`import os`
`import sys`
`conda install pycodestyle`

#Code

- math_lib is a module that takes a list and returns the mean and standard deviation functions are named *mean* and *stdev*, respectively, of that list. In case of a list that contains a non int or float value, the calculations will be performed, but that item in the list will be excluded.

- get_data.py has a function called read_stdin_col() takes a column number and returns an array with data from that column of a data frame that the user supplies to standard in.

- data_viz.py takes a list and a file name for the output and returns a histogram and boxplot, or both, of the data in the list. The file name supplied cannot already exist in the users' directory.  The functions are called histogram(), boxplot(), and combo().

- viz.py takes a plot type (either histogram or boxplot) from the user, data from standard in (you can use gen_data.sh as an example), and an output file name (just as in data_viz.py , cannot already exist) and returns the plot of your choice.
