import csv
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
import sys,argparse
import os.path
import random

# this script takes a given multifasta and returns n random sequences cut at 200bp upstream and downstream,
# should be used to extract random sequences for validation of the secondary structure pipeline

record_dict = SeqIO.index("C_parapsilosis_CDC317_current_not_feature.fasta", "fasta")
output_handle = open("C_parapsilosis_random_intergenic_regions.fasta", "w")

n=0

recDict = {}
sequences = []
outDict = {}

# make that into a proper dict, for reference purpouse
for key, value in record_dict.items():
    recDict[key] = value.seq

while n < 50:
    arg = random.choice(recDict.keys())
    if len(recDict[arg]) > 600:
        region = recDict[arg][200:-200]
        # create outdict to avoid duplicates
        if arg not in outDict:
            my_seqs = SeqRecord(Seq(str(region),IUPAC), id = arg)

            outDict[arg] = region
            sequences.append(my_seqs)
            n+=1
        
##        
SeqIO.write(sequences,output_handle,"fasta")

