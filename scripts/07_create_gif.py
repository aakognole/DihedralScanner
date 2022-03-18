from sys import argv
from glob import glob
from PIL import Image

resid, a1, a2, a3, a4 = str(argv[1]), str(argv[2]), str(argv[3]), str(argv[4]), str(argv[5])

def create_gif():
    pngs = [Image.open(image) for image in sorted(glob("for_gif*.png"))]
    png_one = pngs[0]
    png_one.save("%s_dihe_%s_%s_%s_%s.gif"%(resid,a1,a2,a3,a4), format="GIF",
                 append_images=pngs, save_all=True, duration=10*len(pngs), loop=0)
    
create_gif()
