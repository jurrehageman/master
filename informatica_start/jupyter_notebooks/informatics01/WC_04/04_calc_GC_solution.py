#!/usr/bin/env python3
#solution for GC calculator

#imports
import sys


def calc_gc(seq):
    #calculates the percentage of each base, the GC and AT percentage. 
    # Returns a dict with the percentages
    base_percentage = {}
    total = len(seq)
    A = seq.count("A")/total*100
    T = seq.count("T")/total*100
    C = seq.count("C")/total*100
    G = seq.count("G")/total*100
    base_percentage.update({"A":A})
    base_percentage.update({"T":T})
    base_percentage.update({"C":C})
    base_percentage.update({"G":G})
    base_percentage.update({"GC":G+C})
    base_percentage.update({"AT":A+T})
    return base_percentage


def print_to_terminal(seq, percentages):
    #print sequence and percentage to terminal
    print("Original seq:", seq)
    print("A:", percentages["A"])
    print("T:", percentages["T"])
    print("C:", percentages["C"])
    print("G:", percentages["G"])
    print("GC:", percentages["GC"])
    print("AT:", percentages["AT"])
    print() #prints empty line


def print_to_file(seq, percentages, output_file_name):
    #makes file object and prints the result to the file
    out_file_obj = open(output_file_name, 'a') #each loop in readfile we append to the file
    print("Original seq:", seq, file=out_file_obj)
    print("A:", percentages["A"], file=out_file_obj)
    print("T:", percentages["T"], file=out_file_obj)
    print("C:", percentages["C"], file=out_file_obj)
    print("G:", percentages["G"], file=out_file_obj)
    print("GC:", percentages["GC"], file=out_file_obj)
    print("AT:", percentages["AT"], file=out_file_obj)
    print("\n", file=out_file_obj) #prints empty line
    out_file_obj.close()



def readfile(input_file_name, output_file_name):
    #reads the text file line by line in a for loop.
    #each line calls the print_to_terminal function
    #and print_to_file function
    file_obj = open(input_file_name)
    for line in file_obj:
        seq = line.rstrip('\n')
        percentages_line = calc_gc(seq)
        print_to_terminal(seq, percentages_line)
        print_to_file(seq, percentages_line, output_file_name)
    file_obj.close()



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