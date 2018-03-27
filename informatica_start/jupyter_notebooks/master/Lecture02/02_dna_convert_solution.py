#!/usr/bin/env python3
#solution for DNA convert

#imports
import sys

#ask user input
dna = input("Provide sequence: ")
#now convert to upper:
dna = dna.upper()
#reverse
rev_dna = dna[::-1]
#complement:
bases = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
comp_dna_list = []
for base in dna:
    comp_base = bases[base]
    comp_dna_list.append(comp_base)
comp_dna = "".join(comp_dna_list)
#reverse complement:
rev_comp_dna = comp_dna[::-1]

print("original:", dna)
print("reverse:", rev_dna)
print("complement:", comp_dna)
print("reverse complement:", rev_comp_dna)

