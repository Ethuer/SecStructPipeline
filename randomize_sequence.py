from random import shuffle
from Bio import SeqIO

def shuffle_word(word):
    word = list(word)
    shuffle(word)
    return ''.join(word)

with open('shuffled_sequences/HE605206_1309133-1311227_original', 'r') as in_raw:
    infile = SeqIO.to_dict(SeqIO.parse(in_raw, "fasta"))

    for key,value in infile.items():
        print key
        if 'HE605206:1309133-1311227' in key:
            print value.seq
            f=0
            for f in range(1,500):
                value.seq = shuffle_word(value.seq)
                f+=1
                print f
                
            print 'new'
            print value.seq

