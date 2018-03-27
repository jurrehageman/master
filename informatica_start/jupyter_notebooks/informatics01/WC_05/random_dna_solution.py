#!/usr/bin/env python3

#imports
import sys
import random


def calc_gc(seq):
    #calculates the percentage of GC in the sequence
    g_count = seq.count("G")
    c_count = seq.count("C")
    gc_perc = (g_count + c_count) / len(seq) * 100
    return gc_perc


def generate_dna(len_dna):
    #generates random DNA with GC percentage between 50 and 60%
    #first set gc_perc to 0 or loop will not run
    gc_perc = 0
    #now start the while loop
    #we use OR and not AND! condition < 50 AND > 60 can not exist! 
    while gc_perc < 50 or gc_perc > 60: 
        #generates random dna sequences
        #define letters to choose from in string (note string is a collection)
        bases = "GATC"
        #make an empty list (avoid string concatenation)
        dna = []
        #start for loop to make random letter
        for i in range(len_dna):
            #add a random letter to the list
            dna.append(random.choice(bases))
        #make a string from the list
        sequence = "".join(dna)
        #calculate GC percentage. If this is either < 50 or > 60, the loop will start again!
        #if this is between 50 and 60 the loop will stop!
        gc_perc = calc_gc(sequence)
    #pack both sequence and GC percentage in a tuple and return
    return (sequence, gc_perc)


def main():
    #generate a dna sequence with length 20
    dna = generate_dna(20)
    #print first element from tuple. This is the sequence.
    print("sequence:", dna[0])
    #print second element from tuple. This is the GC percentage.
    print("GC percentage:", dna[1])
    return


main()


