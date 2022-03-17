# dihedral_pes_psi4

Quick setup to perform a potential energy scan for a dihedral using charmm (MM) and psi4 (QM) for force-field parameterization.

# Usage:

 $ ./run <drude/c36> \<resid\> \<atomname1\> \<atomname2\> \<atomname3\> \<atomname4\>

e.g. ./run c36 buta c1 c2 c3 c4

Need psf and crd files named: \<resid\>.\<c36/drude\>.psf & \<resid\>.\<c36/drude\>.crd

(to generate the psf and crd files for an existing residue use: https://github.com/aakognole/build-a-psf)

# What you need to have:
- CHARMM (https://academiccharmm.org/)
- Psi4 (https://psicode.org/)
- Numpy, Matplotlib
#### Optional
- PyMol (https://anaconda.org/conda-forge/pymol-open-source)

## Example results:

![buta_dihe_c1_c2_c3_c4](https://user-images.githubusercontent.com/15039598/158908793-9386ab2b-97c3-45b6-915e-5bdcc726374f.png)

#### Optional GIF >>

![buta_dihe_c1_c2_c3_c4](https://user-images.githubusercontent.com/15039598/158908680-056d677b-c9b6-4f3c-9b4b-9c5d7978d96b.gif)
