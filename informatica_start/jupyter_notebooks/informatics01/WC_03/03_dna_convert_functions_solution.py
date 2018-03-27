#!/usr/bin/env python3
#solution for DNA convert

#imports
import sys


def is_valid_dna(seq):
    #checks if all letters of seq are valid bases
    valid_dna = "ATCG"
    for base in seq:
        if not base in valid_dna:
            #the break statement is not needed anymore as return automatically breaks the loop.
            return False
    #the loop is finished so we are sure no non-valid bases were encountered.
    #we can return True now
    return True


def reverse_dna(seq):
    #reverse string
    rev_dna = seq[::-1]
    return rev_dna


def complement_dna(seq):
    #return complement dna
    bases = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    comp_dna_list = []
    for base in seq:
        comp_base = bases[base]
        comp_dna_list.append(comp_base)
    comp_dna = "".join(comp_dna_list)
    return comp_dna


def reverse_complement_dna(seq):
    rev_dna = (reverse_dna(seq))
    rev_comp_dna = (complement_dna(seq))
    return rev_comp_dna


def main():
    #catch command line arguments
    args = sys.argv
    #check if sequence is given
    if len(args) < 2:
        print("please provide a sequence")
        print("Program stopping...")
        sys.exit()
    #dna string is second argument
    dna = args[1]
    #now convert to upper:
    dna = dna.upper()
    #check if bases are valid:
    if not is_valid_dna(dna):
        print("Non-valid characters found")
        print("Program stopping...")
        sys.exit()

    #call functions
    rev_dna = reverse_dna(dna)
    comp_dna = complement_dna(dna)
    rev_comp_dna = reverse_complement_dna(dna)

    #print output
    print("original:", dna)
    print("reverse:", rev_dna)
    print("complement:", comp_dna)
    print("reverse complement:", rev_comp_dna)

main()