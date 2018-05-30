import sys


def ask_user_input():
    # ask user input
    dna = input("Provide sequence: ")

    return dna


def reverse_dna(dna):
    # now convert to upper:
    dna = dna.upper()
    # reverse
    rev_dna = dna[::-1]

    return rev_dna


def complement_dna(dna):
    # complement:
    bases = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    comp_dna_list = []
    for base in dna:
        comp_base = bases[base]
        comp_dna_list.append(comp_base)
    comp_dna = "".join(comp_dna_list)

    return comp_dna


def reverse_complement(comp_dna):
    # reverse complement:
    rev_comp_dna = comp_dna[::-1]

    return rev_comp_dna


dna = ask_user_input()
rev_dna = reverse_dna(dna)
comp_dna = complement_dna(dna)
rev_comp_dna = reverse_complement(comp_dna)


print("original:", dna)
print("reverse:", rev_dna)
print("complement:", comp_dna)
print("reverse complement:", rev_comp_dna)
