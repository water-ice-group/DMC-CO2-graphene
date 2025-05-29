import numpy as np
import matplotlib.pyplot as plt
from ase.io import read
from copy import deepcopy
from mace.calculators import mace_mp


atoms1 = read("POSCAR_far")
atoms2 = read("POSCAR_graphene")
atoms3 = read("POSCAR_co2")

atoms1.calc = mace_mp('mace-mpa-0-medium.model',dispersion=True,device='cpu')
e1=atoms1.get_potential_energy()

atoms2.calc = mace_mp('mace-mpa-0-medium.model',dispersion=True,device='cpu')
e2=atoms2.get_potential_energy()

atoms3.calc = mace_mp('mace-mpa-0-medium.model',dispersion=True,device='cpu')
e3=atoms3.get_potential_energy()

# print SZ error in meV
with open("SIZE_CONSISTENCY_MLIP_DATA", "a") as f:
    f.write(f"MACE-MPA-0-D3 {1000*(e1-e2-e3)}\n")
f.close()
