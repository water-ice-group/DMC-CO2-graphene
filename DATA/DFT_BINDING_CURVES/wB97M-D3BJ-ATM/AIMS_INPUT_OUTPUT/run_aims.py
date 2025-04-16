import numpy as np
from ase.io import write, read


# Define AIMS calculators for intra energy 
from ase.calculators.aims import Aims, AimsProfile
aims = Aims(
    override_warning_libxc='True',
    xc='libxc HYB_GGA_XC_WB97X_V',
    d3='damping=rational s6=1.0000 a1=0.0000 s8=0.2641 a2=5.4959 s9=0',
    spin='none',
    charge=0,
    relativistic='atomic_zora scalar',
    k_grid=[2,2,1],
    symmetry_reduced_k_grid=False,
    sc_accuracy_rho=1e-7,
    species_dir='/rds/project/rds-Uqezk0eGY00/dellapia/Angstrom/csp/train_set/4K_8K/xdm_species_dir',  # Update to point to species files
    profile=AimsProfile(command=os.environ['ASE_AIMS_COMMAND'])
) 


# example to output total energy
atoms = read('POSCAR')
atoms.calc = aims
atoms.get_potential_energy()
