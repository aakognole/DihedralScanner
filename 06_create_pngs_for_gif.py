import matplotlib.pyplot as plt
import numpy as np
from sys import argv
import os
from glob import glob
from PIL import Image

resid, a1, a2, a3, a4 = str(argv[1]), str(argv[2]), str(argv[3]), str(argv[4]), str(argv[5])

mme = np.loadtxt("%s_dihe_%s_%s_%s_%s.mme"%(resid,a1,a2,a3,a4))
qme = np.loadtxt("%s_dihe_%s_%s_%s_%s.qme"%(resid,a1,a2,a3,a4))
mme_min = min(mme[:,1])
qme_min = min(qme[:,1])

for i,j in enumerate(mme[:,0]):
    mme[i,1] = mme[i,1] - mme_min
    qme[i,1] = qme[i,1] - qme_min

objs = []
pdbs = sorted(glob('*psi4.pdb'))
for i in pdbs:
    obj = list(i.split("_"))
    objs.append((obj[1],obj[2]))
objs = np.array(objs)

for i,j in enumerate(objs[:,0]):
    fig = plt.figure(figsize=(8, 4))
    plt.suptitle("%s : %s-%s-%s-%s = %s"%(resid.upper(),a1.upper(),a2.upper(),a3.upper(),a4.upper(),objs[i,1]))
    plt.subplot(121)
    plt.xlim((np.min(qme[:,0]),np.max(qme[:,0])))
    plt.ylim((0,1.1*max(np.max(qme[:,1]),np.max(mme[:,1]))))
    plt.plot(qme[:,0],qme[:,1], label='QM')
    plt.plot(mme[:,0],mme[:,1], label='MM')
    plt.plot(qme[i,0],qme[i,1], 'o', color="xkcd:black")
    plt.plot(mme[i,0],mme[i,1], 'o', color="xkcd:black")
    plt.xlabel('Dihedral angle (deg)')
    plt.ylabel('Potential energy (kcal/mol)')
    plt.legend()
    plt.subplot(122)
    im = plt.imread(pdbs[i][0:-4]+'.png')
    plt.imshow(im, aspect='equal',alpha=1.0,zorder=10)
    plt.tick_params(
        axis='both',          # changes apply to the x-axis
        which='both',      # both major and minor ticks are affected
        bottom=False,      # ticks along the bottom edge are off
        top=False,         # ticks along the top edge are off
        left=False,
        right=False,
        labelbottom=False,
        labelleft=False) # labels along the bottom edge are off
    plt.tight_layout()
    plt.savefig("for_gif_%s_%s.png"%(objs[i,0],objs[i,1]), dpi=300)
    plt.close()

def create_gif():
    pngs = [Image.open(image) for image in sorted(glob("for_gif*.png"))]
    png_one = pngs[0]
    png_one.save("%s_dihe_%s_%s_%s_%s.gif"%(resid,a1,a2,a3,a4), format="GIF",
                 append_images=pngs, save_all=True, duration=10, loop=0)
    
create_gif()
