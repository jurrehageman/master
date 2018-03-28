#!/usr/bin/env python3

#module imports
import sys


def reverse_complement_dna(seq):
    bases = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    comp_dna_list = []
    for base in seq:
        comp_base = bases[base]
        comp_dna_list.append(comp_base)
    comp_dna = "".join(comp_dna_list)
    rev_comp_dna = comp_dna[::-1]
    return rev_comp_dna


def write_file(file_name, rev_comp_seq):
    '''writes the file'''
    with open(file_name, 'a') as out_file_obj: #note the use of the with statement
        out_file_obj.write(rev_comp_seq + '\n')


def read_file(in_file_name, out_file_name):
    '''reads the file'''
    with open(in_file_name) as in_file_obj: #note the use of the with statement
        for line in in_file_obj:
            seq = line.strip() #strip any whitespace from line
            rev_comp = reverse_complement_dna(seq)
            write_file(out_file_name, rev_comp)


def main():
    '''main function that calls the other functions'''
    #catch command line args
    in_file_name = sys.argv[1]
    out_file_name = sys.argv[2]
    read_file(in_file_name, out_file_name)
    print('all data from',  in_file_name, 'made reverse complement and written to:', out_file_name)


main() #call the main function