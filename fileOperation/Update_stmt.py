# import packages
import os
import string

# Read files
f = open("Input_File", "r")

f1 = open("Output_File", "w")

# Search String
st1 = ""

# Set string
st2 = ""

cnt = 0

lines = f.readlines()

for line in lines:
    if st1 in line:
        st3 = line[168:180]
        st4 = st3.replace('/', '-')
        j = line.index(st1)
        k = len(st1) + j
        m = k + 38

        st5 = st2 + st4 + ' String' + line[k:m] + ';'
        f1.write(st5 + "\n")
    else:
        f1.write(line)
