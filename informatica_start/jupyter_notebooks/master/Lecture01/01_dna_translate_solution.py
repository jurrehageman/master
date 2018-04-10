#!/usr/bin/env python3
# solution for DNA convert from lecture1


# define a DNA sequence and assign it to a variable
DNA = "ATGAGTAGGATAGGCTAGATGGCGATGAATT"

# Always check variables by printing them to screen!
print("DNA sequence: ", DNA)

# check if we have a DNA sequence and not DNA
# DNA does not have the U in the sequence, so lets check this
# we use the string method find() to look for the U character
# find() returns a -1 if nothing was found, so we should set our condition equal to this value
if DNA.find("U") == -1:
    # Using indentation we can define here our block that should be executed if the previous line evaluated to true

    # Reverse the sequence using string slicingand assign it to a new variable named DNA_reversed,
    # remember the -1 step? string[start:stop:step]
    DNA_reversed = DNA[::-1]

    # print the reversed DNA sequence to screen
    print("DNA reversed: ", DNA_reversed)

    # Change the T from DNA to the U in RNA and save it in a new variable
    RNA = DNA_reversed.replace("T", "U")

    # Lastly, print the RNA sequence
    print("RNA sequence: ", RNA)
