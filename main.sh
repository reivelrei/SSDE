SHELL=/bin/bash


# Path to TAIR
TAIR='input/TAIR10.fa'

# Path to DATASET
DATASET='input/Dataset_B.bed'


# Automatische Path Anpassungen
TAIRFAI=${TAIR}.fai
SIZES=${TAIR%.*}.sizes
SLOP=${DATASET/input/"slop"}
X=${SLOP/slop/"getfasta"}
GETFASTA=${X%.*}.fasta
RNAFOLD=${GETFASTA/getfasta/"RNAfold"}


# wird benötigt, um die chrom.sizes zu ermitteln
samtools faidx $TAIR
cut -f 1,2 $TAIRFAI > $SIZES

# vergrößert die Breite um -b
bedtools slop -i $DATASET -g $SIZES -b 40 > $SLOP

# extrahiert die .fasta Dateien
bedtools getfasta -fi $TAIR -bed $SLOP > $GETFASTA

# faltet die .fasta Dateien mit angegebener -T Temperatur
RNAfold -T 20 < $GETFASTA > $RNAFOLD
