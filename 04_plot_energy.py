import matplotlib.pyplot as plt
import numpy as np
from sys import argv
import os

resid, a1, a2, a3, a4 = str(argv[1]), str(argv[2]), str(argv[3]), str(argv[4]), str(argv[5])

mme = np.loadtxt("%s_dihe_%s_%s_%s_%s.mme"%(resid,a1,a2,a3,a4))
qme = np.loadtxt("%s_dihe_%s_%s_%s_%s.qme"%(resid,a1,a2,a3,a4))
mme_min = min(mme[:,1])
qme_min = min(qme[:,1])

for i,j in enumerate(mme[:,0]):
    mme[i,1] = mme[i,1] - mme_min
    qme[i,1] = qme[i,1] - qme_min

plt.figure()
plt.title("resid: %s\ndihe: %s-%s-%s-%s"%(resid.upper(),a1.upper(),a2.upper(),a3.upper(),a4.upper()))
plt.plot(qme[:,0],qme[:,1], label='qme')
plt.plot(mme[:,0],mme[:,1], label='mme')
plt.xlabel('dihedral (deg)')
plt.ylabel('potential energy (kcal/mol)')
plt.legend()
plt.tight_layout()
plt.savefig("%s_dihe_%s_%s_%s_%s.png"%(resid,a1,a2,a3,a4), dpi=300)
plt.close()
