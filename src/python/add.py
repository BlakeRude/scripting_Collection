#!/usr/bin/env python

# Author: Blake Rude
# 
# This script takes the name of a file
# and then adds line numbers to each line
#
# 3 May 2019

path = raw_input("Give file name ")

outfile = open("./NEW_FILE.txt", 'w')
with open(path, 'r') as infile:
    line = infile.readline()
    type(line) is long
    n = 1
    while line:
        # Have a 0 at the front for numbers with less than two digits
        if ( n < 10 ): 
            outfile.write("0{} {}\n".format(n, line.strip()))
        # If it has two, no 0 at the front
        else:
            outfile.write("{} {}\n".format(n, line.strip()))
        line = infile.readline()
        n+= 1
infile.close
outfile.close
print("NEW_FILE.txt Created.")
