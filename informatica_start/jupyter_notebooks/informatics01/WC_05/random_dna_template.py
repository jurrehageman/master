#!/usr/bin/env python3

#imports
import sys
import random


def calc_gc(seq):
    #calculates the percentage of GC in the sequence
    #finish this function yourself
    pass


def generate_dna(len_dna):
    #generates random DNA with GC percentage between 50 and 60%
    #some comments removed. Write your own comments!
    gc_perc = ?
    while gc_perc < ? ? gc_perc > ?: 
        bases = ?
        #make an empty list (avoid string concatenation)
        dna = ?
        #start for loop to make random letter
        for i in range(?):
            #add a random letter to the list
            dna.append(?)
        #make a string from the list
        sequence = "".join(?)
        #calculate GC percentage. If this is either < 50 or > 60, the loop will start again!
        #if this is between 50 and 60 the loop will stop!
        gc_perc = ?(?)
    #pack both sequence and GC percentage in a tuple and return
    return (?, ?)


def main():
    #generate a dna sequence with length 20
    dna = generate_dna(20)
    #print first element from tuple. This is the sequence.
    print("sequence:", dna[0])
    #print second element from tuple. This is the GC percentage.
    print("GC percentage:", dna[1])
    return


main()


