#!/usr/bin/python

##THIS SCRIPT IS MEANT TO COMPARE TECHNICAL REPLICATES TO SEE ERROR RATES OF SEQUENCING
##FOR ALL SITES WHICH BOTH TECHNICAL REPLICATES SHARE SEQUENCE, THEY SHOULD HAVE THE SAME SNPs

import sys
import itertools
from Bio import SeqIO
import numpy as np

infile = sys.argv[1]
snp_loc_file = sys.argv[2]
outfile = sys.argv[3]
data = open(infile).readlines()
out = open(outfile,'w')
snp = open(snp_loc_file, 'w')

line1 = data[1].lstrip().rstrip().split(" ")
line2 = data[2].lstrip().rstrip().split(" ")

match_vector = []
snp_location = []
for i in range(len(line1[3])):
    if line1[3][i] != 'N':
        if line2[3][i] != 'N':
            snp_location.append(i)
            if line1[3][i] == line2[3][i]:
                match_vector.append('1')
            else:
                match_vector.append('0')

snp_location = [str(i) for i in snp_location]

snp.write(" ".join(snp_location))
out.write(" ".join(match_vector))

out.close()              
snp.close()
    
