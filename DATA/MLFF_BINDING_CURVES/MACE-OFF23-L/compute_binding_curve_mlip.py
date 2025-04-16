from ase.io import read, write
import numpy as np
from mace.calculators import MACECalculator
from mace.calculators import mace_off

# define the calculator

mlip = mace_off(model='large',device='cpu')


# load the trajectory
traj = read('TRAJECTORY.extxyz',':')

data = []

for atoms in traj:

    atoms.calc = mlip

    # Compute the energy
    e = atoms.get_potential_energy()

    # Compute CO2 position relative to graphene
    z_c = atoms.positions[50,2]
    z_gra = np.mean(atoms.positions[:50,2])
    distance = z_c - z_gra

    #  update data
    data.append([distance,e])
data = np.array(data)


# Save data into ENERGY_vs_DISTANCE
np.savetxt('ENERGY_vs_DISTANCE', data, header="C-Distance [A] Energy [eV]")

# Compute binding energy as  Total_Energy - Total_energy[-1] , i.e. E[co2+graphene] - E[co2 --- graphene]
binding_energy = data.copy()
binding_energy[:,1] -= binding_energy[-1,1]


np.savetxt('BINDING_ENERGY_vs_DISTANCE', binding_energy, header="C-Distance [A] BindingEnergy [eV]")
