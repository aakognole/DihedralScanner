# dihedral_pes_psi4
to perform a potential energy scan for a dihedral using charmm and psi4

Usage: ./run <drude/c36> \<resid\> \<atomname1\> \<atomname2\> \<atomname3\> \<atomname4\>

e.g. ./run c36 gln CB CG CD NE2

Need psf and crd files named: \<resid\>.\<c36/drude\>.psf & \<resid\>.\<c36/drude\>.crd
