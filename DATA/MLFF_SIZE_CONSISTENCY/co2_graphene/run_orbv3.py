import numpy as np
import matplotlib.pyplot as plt
from ase.io import read
from copy import deepcopy
from orb_models.forcefield import pretrained
from orb_models.forcefield.calculator import ORBCalculator

# define the calculator
device="cpu" 
orbff = pretrained.orb_v3_conservative_inf_omat(device=device)
calc = ORBCalculator(orbff, device=device)

# Load structure

atoms1 = read("POSCAR_1")
atoms2 = read("POSCAR_2")
atoms3 = read("POSCAR_3")


atoms1.calc = calc
e1=atoms1.get_potential_energy()

atoms2.calc = calc
e2=atoms2.get_potential_energy()

atoms3.calc = calc
e3=atoms3.get_potential_energy()


print(1000*(e1-e2-e3))
