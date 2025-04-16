import numpy as np
from ase.io import write, read


# Define AIMS calculators for intra energy 
from ase.calculators.aims import Aims, AimsProfile
aims = Aims(
    xc='pbe0',
    d3='damping=zero',
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
