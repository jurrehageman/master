#!/usr/bin/env python3
#template for GC calculator:

#imports
import sys


def calc_gc(seq):
    #calculates the percentage of each base, the GC and AT percentage. 
    # Returns a dict with the percentages
    pass


def print_to_terminal(seq, percentages):
    #print sequence and percentage to terminal
    pass


def print_to_file(seq, percentages, output_file_name):
    #makes file object and prints the result to the file
    pass


def readfile(input_file_name, output_file_name):
    #reads the text file line by line in a for loop.
    #each line calls the print_to_terminal function
    #and print_to_file function
    pass



def main():
    #main function:
    #catch command line arguments
    args = sys.argv
    #check if file names are given
    if len(args) < 3:
        print("please provide the name of an input and an output file")
        print("Program stopping...")
        sys.exit()
    input_file_name = args[1]
    output_file_name = args[2]
    
    #call functions
    readfile(input_file_name, output_file_name)

#call the main function
main()