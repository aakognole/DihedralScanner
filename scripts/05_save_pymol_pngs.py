import pymol
pymol.finish_launching([ 'pymol', '-qc'])

from glob import glob
from sys import argv

a1, a2, a3, a4 = str(argv[1]).upper(), str(argv[2]).upper(), str(argv[3]).upper(), str(argv[4]).upper()

pymol.cmd.do("set ray_shadows,0")
pymol.cmd.do("set orthoscopic, on")

pdbs = sorted(glob('*psi4.pdb'))
for i,j in enumerate(pdbs):
    k = j.split("_")[1]
    print(k)
    pymol.cmd.load(j)
    if not i == 0:
        pymol.cmd.align("%s and (name %s or name %s or name %s)"%(j[0:-4], a1, a2, a3),"%s and (name %s or name %s or name %s)"%(pdbs[0][0:-4], a1, a2, a3))
        pymol.cmd.disable("%s"%(pdbs[0][0:-4]))
    pymol.cmd.util.cbag(j[0:-4])
    pymol.cmd.zoom("all")
    pymol.cmd.do("label name %s or name %s or name %s or name %s, name"%(a1, a2, a3, a4))
    pymol.cmd.do("set label_color, black, all")
    pymol.cmd.do("set label_font_id, 7")
    pymol.cmd.do("set label_size, -0.25")
    pymol.cmd.do("set label_outline_color, white")
    pymol.cmd.png("%s.png"%(j[0:-4]), dpi=300, ray=1)
    if not i == 0:
        pymol.cmd.delete(j[0:-4])

pymol.cmd.quit()

