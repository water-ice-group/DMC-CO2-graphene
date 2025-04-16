import numpy as np
import os, shutil
from ase import Atoms
from ase.io import write, read
from copy import deepcopy


# Define AIMS calculators for intra energy 
from ase.calculators.aims import Aims, AimsProfile
aims = Aims(
    xc='b86bpbe',
    xdm='0.90036995  0.78080929',
    spin='none',
    charge=0,
    relativistic='atomic_zora scalar',
    k_grid_density=1,
    symmetry_reduced_k_grid=False,
    sc_accuracy_rho=1e-7,
    species_dir='/rds/project/rds-Uqezk0eGY00/dellapia/Angstrom/csp/train_set/4K_8K/xdm_species_dir',  # Update to point to species files
    profile=AimsProfile(command=os.environ['ASE_AIMS_COMMAND'])
)  



traj = read('trajectory.extxyz',':')

data = []
for idx, atoms in enumerate(traj):

    try:
        del atoms.calc
        atoms.calc = aims
        e = atoms.get_potential_energy()
        shutil.copy('aims.out','aims_'+str(idx)+'.out')
        
        z_c = atoms.positions[50,2]
        z_gra = np.mean(atoms.positions[:50,2])
        distance = z_c - z_gra
        data.append([distance,e])
    except Exception as e:
        print(e)



data = np.array(data)
np.savetxt('ENERGY_vs_DISTANCE', data, header="C-Distance [A] Energy [eV]")

binding_energy = data.copy()
binding_energy[:,1] -= binding_energy[-1,1]

np.savetxt('BINDING_ENERGY_vs_DISTANCE', binding_energy, header="C-Distance [A] BindingEnergy [eV]")
