from random import shuffle
from Bio import SeqIO
import sys,argparse
import os.path
import csv

#####################################################################################################
# sequence shuffler,   takes input fasta sequence and returns a shuffled input fasta sequence       #
# default 500 iterations of shuffle()                                                               #
#############################(C) Ethur ##############################################################

# arguments for commandline input and help
####################################################
parser = argparse.ArgumentParser(description='This script takes a multifasta file, and queries against a blastdb, returning hits and score')
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
                    help='Output a fasta file containing the shuffled sequence',
                    metavar = 'FILE',
                    #type=argparse.FileType('w')
                    )

parser.add_argument('-iter',
                    dest='iter',
                    required = False,
                    default='500',
                    help='amount of iterations of shuffle that are called on the input fasta',
                    metavar = 'integer',
                    #type=argparse.FileType('w')
                    )


args = parser.parse_args()


def shuffle_word(word):
    word = list(word)
    shuffle(word)
    return ''.join(word)

with open('%s' %(args.fasta), 'r') as in_raw,open('%s'%(args.output), 'w') as out_raw :
    infile = SeqIO.to_dict(SeqIO.parse(in_raw, "fasta"))
    outfile = csv.writer(out_raw, delimiter = ' ')
    for key,value in infile.items():
        #print key

        #print value.seq
        f=0
        for f in range(1,int(args.iter)):
            value.seq = shuffle_word(value.seq)
            f+=1
            #print f
                
                
        #print 'new'
        #print value.seq
        
        outfile.writerow(['>',key])
        outfile.writerow([value.seq])
