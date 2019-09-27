import data_viz

def main(plot_type,output_file_name):
    D=[]
    for l in sys.stdin():
        A=l.rstrip().split()
        D.append(float(A[0]))
        D.append(float(A[1]))

    if plot_type='histogram':
        return data_viz.histogram(D,output_file_name)
    else:
        if plot_type='boxplot':
            return data_viz.boxplot(D,output_file_name)
        else:
            return 'I cannot plot in that way.'


if __name__ == '__main__':
    main()
