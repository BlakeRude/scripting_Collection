#!/usr/bin/env python

# Author: Blake Rude
# 
# This script takes the name of a file which has line numbers
# and then removes the line numbers from each line
#
# 3 May 2019

path = raw_input("Give file name ")

outfile = open("./NEW_FILE.txt", 'w')
with open(path, 'r') as infile:
    line = infile.readline()
    n = 1
    while line:
        outfile.write(line[3:])
        line = infile.readline()
        n+= 1
infile.close
outfile.close
print("NEW_FILE.txt Created.")
