import os
from sys import argv
#print ("Usage: Takes in pdb or xyz file format. Prints out Psi4 input.")

f=open(argv[1],'r')
fr=f.readlines()
coor=''

d = {}
i = 1

if argv[1].split('.')[-1]=='pdb':
    for line in fr:
        if line.startswith("ATOM"):
           field=line.split()
           if field[2][0] != 'D' and field[2][0:2] != 'LP':
               d[field[2]] = i
               coor=coor+" ".join([field[2][0],field[5],field[6],field[7],"\n"])
               i += 1

elif argv[1].split('.')[-1]=='xyz':
    for line in fr[2:]:
        field=line.split()
        if len(field)!=4: continue
        coor=coor+" ".join([field[0],field[1],field[2],field[3],"\n"])

temp="""
molecule {
%s
}

set basis 6-31+G(d)

set optking {
  frozen_dihedral = ("
    %d %d %d %d  
  ")
}
optimize('mp2')
"""

a1,a2,a3,a4 = d[str(argv[2]).upper()],d[str(argv[3]).upper()],d[str(argv[4]).upper()],d[str(argv[5]).upper()]

print (temp%(coor,a1,a2,a3,a4))
