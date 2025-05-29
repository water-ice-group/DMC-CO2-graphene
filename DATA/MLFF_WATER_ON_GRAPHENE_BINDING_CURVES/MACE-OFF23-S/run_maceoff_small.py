import numpy as np
import matplotlib.pyplot as plt
from ase.io import read
from copy import deepcopy
from mace.calculators import mace_off

# Load initial structure
atoms = read("POSCAR")

# Identify graphene and molecule  atoms
z_positions = np.array([atom.position[2] for atom in atoms])
element_symbols = [atom.symbol for atom in atoms]

graphene_indices = [i for i, (z, s) in enumerate(zip(z_positions, element_symbols)) if z < 1.0 and s == 'C']
graphene_z_avg = np.mean([z_positions[i] for i in graphene_indices])

h2o_indices = [i for i in range(len(atoms)) if i not in graphene_indices]
h2o_O_index = [i for i in h2o_indices if atoms[i].symbol == 'O'][0]
h2o_O_z_orig = atoms[h2o_O_index].position[2]

# array of distances
target_distances = np.linspace(2.5, 10.0, 25)

# calculator
calc = mace_off(model='small', device='cpu')

# Store energies and Z distances
energies = []
z_diffs = []

# Loop over distances
for target_z in target_distances:
    atoms_copy = deepcopy(atoms)
    delta_z = target_z - (h2o_O_z_orig - graphene_z_avg)

    for i in h2o_indices:
        atoms_copy[i].position[2] += delta_z
    atoms_copy.calc = calc

    energy = atoms_copy.get_potential_energy()
    z_actual = atoms_copy[h2o_O_index].position[2] - graphene_z_avg

    z_diffs.append(z_actual)
    energies.append(energy)

binding_energy = np.array(energies) - energies[-1]

data = np.column_stack((z_diffs, energies, binding_energy))
# save 
np.savetxt("DISTANCE_TOTALENERGY_BINDINGENERGY.txt", data,
           header="Distance(A) TotalEnergy(eV) BindingEnergy(eV)",
           fmt="%.8f")

# plot
plt.figure(figsize=(8, 5))
plt.plot(z_diffs, 1000*binding_energy, '-o')
plt.xlabel('Distance [A]')
plt.ylabel('Interaction energy [eV]')
plt.grid(True)
plt.tight_layout()
plt.show()

