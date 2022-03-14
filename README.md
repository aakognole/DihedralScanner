# dihedral_pes_psi4

Quick setup to perform a potential energy scan for a dihedral using charmm (MM) and psi4 (QM) for force-field parameterization.

# Usage:

 $ ./run <drude/c36> \<resid\> \<atomname1\> \<atomname2\> \<atomname3\> \<atomname4\>

e.g. ./run c36 buta c1 c2 c3 c4

Need psf and crd files named: \<resid\>.\<c36/drude\>.psf & \<resid\>.\<c36/drude\>.crd

# What you need to have:
- CHARMM (https://academiccharmm.org/)
- Psi4 (https://psicode.org/)
- Numpy, Matplotlib 