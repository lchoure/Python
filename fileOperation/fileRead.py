# import packages
import os

#delete files

f = open("C:\\Users\\A9884\\Downloads\\EDIVZ.DRFEHL.SCHQOSA.#240916.txt","r")
f1 = open("C:\\Users\\A9884\\Downloads\\GF#.txt","w")
f2 = open("C:\\Users\\A9884\\Downloads\\sp.txt","w")

st1 = 'SCHADEN.GF#='
st2 = 'N='
st3 = 'NO TOLERANCE FOUND'

cnt = 0
cnt1 = 0

lines = f.readlines()

# get the all Gf#
for line in lines:
    if st1 in line:
        j = line.index(st1)
        k = len(st1) + 1
        m = k + 36
        f1.write("\'{0}\',\n".format(line[k:m]))
        cnt += 1

# get sparte eigen
for line in lines:
    if st2 in line:
       i = line.index(st2) + 2
       f2.write(line[i:i+2] + "\n")

#get error count
for line in lines:
    if st3 in line:
        cnt1 += 1

print(cnt)
print(cnt1)
f1.close()
f2.close()
f.close()


#print(f.read())