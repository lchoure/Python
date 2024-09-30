# import packages
import os

#Read files
f = open("C:\\Users\\A9884\\Python\\Ext_Files\\INSERTS UMTX-26006.sql","r")
f1 = open("C:\\Users\\A9884\\Python\\Ext_Files\\Update.txt","w")

st1 = "VALUES ("

st2 = "UPDATE ABS.TSCHADEN_GEN SET="

cnt = 0

lines = f.readlines()

# get the all Gf#
for line in lines:
    if st1 in line:
        st3 = line[168:180]
        st4 = st3.replace('/','-')
      #  print(line.index('06/09/2024'))
        j = line.index(st1)
        k = len(st1) + j 
        m = k + 38
               # print("\'{0}\'".format(line[k:m]))
        cnt += 1

        st5 = st2 + st4 + ' WHERE SGEN#=' + line[k:m] + ';'
        print(st5)
    else:
        print(format(line))
      