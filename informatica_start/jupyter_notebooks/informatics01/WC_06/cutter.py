#!/usr/bin/env python3
#template for script:

#imports
import sys

#global variables


def valid_enzyme(enzyme):
    #checks if valid enzyme is provided
    enzymes = ['ECOR1', 'BAMH1', 'HIND3']
    if enzyme in enzymes:
        return True
    else:
        return False


def has_restriction_site(seq, site):
    #checks is a site is present
    sites = {"ECOR1":"GAATTC", "BAMH1":"GGATTCC", "HIND3":"AAGCTT"}
    if sites[site] in seq:
        return True
    else:
        return False


def get_fragments(seq, site):
    #generates the fragments
    sites = {"ECOR1":"GAATTC", "BAMH1":"GGATTCC", "HIND3":"AAGCTT"}
    #all cutt after first nucleotide
    offset = 1
    cut_position = seq.find(sites[site]) + offset
    seq_size = len(seq)
    fragment_sizes = (cut_position, seq_size - cut_position)
    return fragment_sizes
    


def pretty_print(seq, site, fragments):
    #prints the results to the terminal
    if fragments:
        print("Sequence:", seq)
        print("Enzyme", site , "creates fragments of:")
        for i in fragments:
            print(i, "bp")
    else:
        print("Sequence:", seq)
        print("No cut site found")



def main():
    #main function:
    #catch command line arguments
    args = sys.argv
    #check if file names are given
    if len(args) < 3:
        print("please provide a sequence followed by an enzyme (bamh1, ecor1, hind3)")
        print("Program stopping...")
        sys.exit()
    input_sequence = args[1].upper()
    enzyme = args[2].upper()
    
    #call functions
    if not valid_enzyme(enzyme):
        print(enzyme, "is not a valid enzyme")
        sys.exit()
    site_present = has_restriction_site(input_sequence, enzyme)
    fragments = None
    if site_present:
        fragments = get_fragments(input_sequence, enzyme)
    pretty_print(input_sequence, enzyme, fragments)
    return
    
#call the main function
main()