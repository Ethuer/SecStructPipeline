import csv
import re
import sys,argparse
import os.path

collectdict={}

# This script just adds the lost headers back into the prediction file
# column 1 is the header, column 2 the startpoint  column 3 the probability

# arguments for commandline input and help
####################################################
parser = argparse.ArgumentParser(description='This script takes a parsed prediction result and adds the header')
parser.add_argument('-pred',
                    dest='pred',
                    required = True,
                    help='Input a parsed RNAfold prediction file, to extract the header',
                    metavar = 'FILE',
                    #type=lambda x: is_valid_file(parser,x)
                    )

parser.add_argument('-res',
                    dest='res',
                    required = True,
                    help='Input a results probablilty file to extract the probabilities',
                    metavar = 'FILE',
                    #type=lambda x: is_valid_file(parser,x)
                    )


parser.add_argument('-out',
                    dest='output',
                    required = False,
                    default='output.fasta',
                    help='Output a concatenated file of probabilities witht their header',
                    metavar = 'FILE',
                    #type=argparse.FileType('w')
                    )


args = parser.parse_args()

# populate dictionary
def collection(ref_file):
    counter = 0
    for row in ref_file:
        if '>' in row[0]:
            counter +=1
            collectdict[counter]= row[0]
    return collectdict


with open('%s'%(args.pred), 'r') as ref_raw, open('%s' %(args.res),'r') as in_raw, open('%s' %(args.output),'w') as out_raw:
    ref = csv.reader(ref_raw,delimiter=',')
    infile = csv.reader(in_raw,delimiter=',')
    outfile = csv.writer(out_raw, delimiter='\t')
    infile.next()
    
    coll_dict = collection(ref)
    
    for rown in infile:
        #print coll_dict[int(rown[0])], rown[1]
        outfile.writerow([coll_dict[int(rown[0])].split(' ')[1],coll_dict[int(rown[0])].split(' ')[2], rown[1]])
