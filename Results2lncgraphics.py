import csv
import numpy as np
##import matplotlib.mlab as mlab
import numpy as np
import matplotlib.pyplot as plt
import sys,argparse
import os.path

# arguments for commandline input and help
####################################################
parser = argparse.ArgumentParser(description='This script prints out a vline plot of the predicted structural conservation')
parser.add_argument('-in',
                    dest='infile',
                    required = True,
                    help='',
                    metavar = 'FILE',
                    #type=lambda x: is_valid_file(parser,x)
                    )

args = parser.parse_args()



with open('%s' %(args.infile),'r') as in_raw:
    infile = csv.reader(in_raw, delimiter='\t')

    y = []
    x = []


    for row in infile:
        y.append(row[1])
        x.append(row[2])

    print '%s'%(args.infile)
    fig = plt.figure()
    ax1 = fig.add_subplot(211)
    ax1.plot(y,x)
    ax1.set_title('%s'%(args.infile))
    ax1.vlines(y,[0],x,label='%s'%(args.infile))
    
    plt.show()
