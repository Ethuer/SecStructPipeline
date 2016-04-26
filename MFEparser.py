import csv
import re
import sys,argparse
import os.path


#####################################################################################################
# Resultparsing script, extracts the windowname and the MFE score                                   #
#                                                                                                   #
#############################(C) Ethur ##############################################################
#
# arguments for commandline input and help
####################################################
parser = argparse.ArgumentParser(description='This script takes a prediction result and extracts the MFE value')
parser.add_argument('-pred',
                    dest='pred',
                    required = True,
                    help='Input a RNAfold prediction file containing the full predictions',
                    metavar = 'FILE',
                    #type=lambda x: is_valid_file(parser,x)
                    )


parser.add_argument('-out',
                    dest='output',
                    required = False,
                    default='output.fasta',
                    help='Output a file containing the names of sequences and their mfe value',
                    metavar = 'FILE',
                    #type=argparse.FileType('w')
                    )


args = parser.parse_args()

with open('%s' %(args.pred),'r') as in_raw,open('%s' %(args.output),'w') as out_raw:
    infile = csv.reader(in_raw, delimiter='\t')
    outfile = csv.writer(out_raw, delimiter = ' ')
    
    for row in infile:
##        if 'HE6' in row[0]:
##            print row[0]
##            outfile.writerow([row[0]])
        if '(  0.00)' in row[0]:
##            print '-0.01'
            outfile.writerow(['-0.01'])
            #argument = int(0.01)
        else:
            argument = re.search('-\d{1,2}.\d{2}\)',row[0])         
        if argument:
##            print row
            argument = re.search('-\d{1,2}.\d{2}',argument.group(0))
##            print argument.group(0)
            outfile.writerow([argument.group(0)])
        
                        

