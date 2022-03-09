import numpy as np
from sys import argv
import os

resid, a1, a2, a3, a4 = str(argv[1]), str(argv[2]), str(argv[3]), str(argv[4]), str(argv[5])

a = np.loadtxt('output/mm_%s_dihe_%s_%s_%s_%s.txt'%(resid,a1,a2,a3,a4))

emin = min(a[:,1])
mme = []
iters = []

for i,e in enumerate(a[:,1]):
    if e < emin+15:
        mme.append((a[i,0],a[i,1],a[i,2]))

mme = np.array(mme)
a = mme[mme[:, 0].argsort()]

for i,j in enumerate(a[:,0]):
    try:
        if a[i+1,0]-j > 30:
            for l in range(i+1):
                a[l,0] = a[l,0] + 360.0
            break
    except IndexError:
        break

f = open('output/%s_dihe_%s_%s_%s_%s.mme'%(resid,a1,a2,a3,a4), 'w')
a = a[a[:, 0].argsort()]
for i,j in enumerate(a[:,0]):
    f.write("%.2f %.3f %d\n"%(a[i,0],a[i,1],i+1001))
    iters.append((a[i,0],a[i,2],i+1001))
f.close()        

iters = np.array(iters)
path = "output/%s_dihe_%s_%s_%s_%s"%(resid,a1,a2,a3,a4)

for i,j in enumerate(iters[:,1]):
    os.system('cp %s/d_%d.pdb %s/d_%d_%.2f_psi4.pdb'%(path,j,path,iters[i,2],iters[i,0]))
