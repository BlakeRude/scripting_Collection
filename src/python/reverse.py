#!/usr/bin/env python

# Author: Blake Rude
# 
# This script takes the name of a file
# and then reverses all the text in the file
#
# 3 May 2019

path = raw_input("Give filename for reversal ")
infile = open(path, 'r')
outfile = open("REVERSED.txt", 'w')

tmp = []
for line in infile:
    rev = line[::-1]
    tmp.append(rev)

for line in rev:
    outfile.write(line)
infile.close
outfile.close
print("REVERSED.txt Complete.")
