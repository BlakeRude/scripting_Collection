A#!/usr/bin/env python

# Author: Blake Rude
# 
# This script takes the name of a file
# and then changes it's file extention to .cpp
# for different file names, change line 19
#
# 3 May 2019

import os
import glob

files = glob.glob('*.c')
for file in files:
    # Split the filename at the . sp splt[0] = file name without extention
    splt = file.split('.')
    # Give new extention and rename
    new = '{}.cpp'.format(splt[0]) # change this to change what file extention gets appended
    os.rename(file, new)
