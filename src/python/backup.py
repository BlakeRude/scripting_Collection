#!/usr/bin/env python

# Author: Blake Rude
# 
# This script takes all the files in your current working directory
# and creates a backup directory called {CWD}/.backup
#
# 3 May 2019

import os
import glob
import shutil
s = (os.getcwd())
path = (os.getcwd() + "/.backup")
print(path)
files = os.listdir(s)

for f in files:
    shutil.copy(s+"/"+f, path)
