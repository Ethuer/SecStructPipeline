#!/bin/bash

# create target directories

mkdir shuffled_sequences
mkdir windows_of_sequences/
mkdir predictions/
mkdir parsed_pred
mkdir combined
mkdir results


FASTA=$1
OUTFILE=$2
TEMP=$3

echo "[STATUS] starting pipeline at" 
echo `date`
# shuffle sequences 50 times to create the background

for f in {1..50}
do
python Shuffle_sequence.py -fasta $FASTA -out shuffled_sequences/LNCRNA4_shuffle${f}.fa
done


# split into 50 bp windows

# the original sequence
for f in {1..50} ; do
python fasta2_50bpwindows.py -fasta $FASTA -out windows_of_sequences/CDC317_intergen_original.fa_+$f.fa -adv $f
done


# the shuffled sequences
echo "[STATUS] shuffling sequences"
for q in shuffled_sequences/*.fa; do
s=${q#"shuffled_sequences/"}
echo $s
    for f in {1..50} ; do
    #echo $q $f `date`
    python fasta2_50bpwindows.py -fasta $q -out windows_of_sequences/${s}_+$f.fa -adv $f
    done
done

# run RNAFold agains everything
# modifyable,  using default input to RNAfold

echo "[STATUS] running RNAfold"
for f in windows_of_sequences/*.fa ; do
s=${f#"windows_of_sequences/"}
#echo $s `date`
RNAfold --temp=$TEMP --noPS < $f > predictions/$s.pred
done


# parse the output

for f in predictions/*.pred ; do
s=${f#"predictions/"}
python MFEparser.py -pred $f -out parsed_pred/$s
done


# concatenate
echo "[STATUS] Parsing output"
for f in {1..50} ; do 
paste parsed_pred/*original*+${f}.fa.pred parsed_pred/*shuffle*.fa_+${f}.fa.pred | sed 's/\r//g' > combined/CDC317_intergenic_+${f}.noname.combipred 
done

# analyze without header

for f in {1..50} ; do 
Rscript Statistical_analysis.R combined/CDC317_intergenic_+${f}.noname.combipred  results/shuffle${f}
done

# reintroduce header
for f in {1..50} ; do 
python Resultparser.py -pred predictions/CDC317_intergen_original.fa_+${f}.fa.pred -res results/shuffle${f} -out results/shuffle+${f}.txt
done

# concatenate into one file
# sort


# if there is no output name declared, use defaultname

echo "[STATUS] Writing to file"

#if [-z OUTFILE] 
#then
#paste results/shuffle+*.txt | sed 's/\r\t/\n/g' > Transcript_probabilities.txt
#sort -nk 2,2 Transcript_probabilities.txt > Transcript_probabilities.sort.txt
#fi

#if [-n OUTFILE] 
#then
paste results/shuffle+*.txt | sed 's/\r\t/\n/g' > ${OUTFILE}.txt
sort -nk 2,2 ${OUTFILE}.txt > ${OUTFILE}.sort.txt
#fi

# clean directories

echo "[CLEANUP] Compressing output to archives"
tar -zcvf Archive_shuffled_sequences.tar.gz shuffled_sequences/  && rm -R shuffled_sequences/
tar -zcvf Archive_windows_of_sequences.tar.gz windows_of_sequences/  && rm -R windows_of_sequences/
tar -zcvf Archive_predictions.tar.gz predictions/ && rm -R predictions/
tar -zcvf Archive_parsed_pred.tar.gz parsed_pred/ && rm -R parsed_pred/
tar -zcvf Archive_combined.tar.gz combined/ && rm -R combined/
tar -zcvf Archive_results.tar.gz results/ && rm -R results/



