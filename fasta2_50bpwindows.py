import csv
from Bio import SeqIO
import sys,argparse
import os.path

#####################################################################################################
# windowmaker script  creates (default 50bp) windows of input (multi-)fasta files                   #
# default 50bp windows starting at bp1                                                              #
#############################(C) Ethur ##############################################################

# arguments for commandline input and help
####################################################
parser = argparse.ArgumentParser(description='This script takes a multifasta file, and splits it into 50bp sequence windows')
parser.add_argument('-fasta',
                    dest='fasta',
                    required = True,
                    help='Input a multi fasta file containing the original sequence',
                    metavar = 'FILE',
                    #type=lambda x: is_valid_file(parser,x)
                    )


parser.add_argument('-out',
                    dest='output',
                    required = False,
                    default='output.fasta',
                    help='Output a multi fasta file containing the windowed sequence',
                    metavar = 'FILE',
                    #type=argparse.FileType('w')
                    )

parser.add_argument('-ws',
                    dest='iter',
                    required = False,
                    default='50',
                    help='Size of the windows (default = 50bp)',
                    metavar = 'integer',
                    #type=argparse.FileType('w')
                    )

parser.add_argument('-adv',
                    dest='advance',
                    required = False,
                    default='0',
                    help='Tilt of windows. 1 will shift the windows by 1bp downstream (default = 0)',
                    metavar = 'integer',
                    #type=argparse.FileType('w')
                    )

parser.add_argument('-igne',
                    dest='ignore',
                    required = False,
                    default=False,
                    help='ignore the last 50bp window, which will overlap with the secnd to last (default is to keep it = False ) True/False',
                    metavar = 'integer',
                    #type=argparse.FileType('w')
                    )

args = parser.parse_args()

with open('%s'%(args.fasta), 'r') as in_raw, open('%s'%(args.output), 'w') as out_raw :
    infile = SeqIO.to_dict(SeqIO.parse(in_raw, "fasta"))
    outfile = csv.writer(out_raw, delimiter = ' ')

    for key,value in infile.items():
            #print key,len(value.seq)
            start=0
            for f in range(1,len(value.seq)):
                if f%int(args.iter) == 0 :  # create windows via modulo operator
                    f=f+int(args.advance)
                    stop = f
                    start = f-50
                    outfile.writerow(['>', key, start, stop])
##                    print '>', key, start, stop
                    outfile.writerow([value.seq[int(start):int(stop)]])
##                    print value.seq[int(start):int(stop)]
            # write the last 50bp as their own seqment to file,  or ignore it ?
            if args.ignore == False:
                outfile.writerow(['>', key, start, stop])
                #print '>' , len(value.seq)-50,len(value.seq)
                outfile.writerow([value.seq[int(start):int(stop)]])
                #print value.seq[len(value.seq)-50:len(value.seq)]
            
##        print value.seq[1:50]
            
##    row[6]
