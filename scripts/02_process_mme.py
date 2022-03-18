import numpy as np
from sys import argv
import os

# cutoff for the maximum energy from minima to include
cutoff = 15.0 # kcal/mol

resid, a1, a2, a3, a4 = str(argv[1]), str(argv[2]), str(argv[3]), str(argv[4]), str(argv[5])
jobname="%s_dihe_%s_%s_%s_%s"%(resid,a1,a2,a3,a4)

a = np.loadtxt('mm_%s.txt'%(jobname))

emin = min(a[:,1])
mme = []

for i,e in enumerate(a[:,1]):
    if e < emin+cutoff:
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

f = open('%s.mme'%(jobname), 'w')
a = a[a[:, 0].argsort()]
iters = []
for i,j in enumerate(a[:,0]):
    f.write("%.2f %.3f %d\n"%(a[i,0],a[i,1],i+1001))
    iters.append((a[i,0],a[i,2],i+1001))
f.close()        
iters = np.array(iters)

for i,j in enumerate(iters[:,1]):
    os.system('cp d_%d.pdb d_%d_%.2f_psi4.pdb'%(j,iters[i,2],iters[i,0]))
