import numpy as np
import matplotlib.pyplot as plt
from ase.io import read
from copy import deepcopy
from orb_models.forcefield import pretrained
from orb_models.forcefield.calculator import ORBCalculator

device="cpu" 
orbff = pretrained.orb_v3_conservative_inf_omat(device=device)
calc = ORBCalculator(orbff, device=device)


atoms1 = read("POSCAR_far")
atoms2 = read("POSCAR_graphene")
atoms3 = read("POSCAR_co2")


atoms1.calc = ORBCalculator(orbff, device=device)
e1=atoms1.get_potential_energy()

atoms2.calc =  ORBCalculator(orbff, device=device)
e2=atoms2.get_potential_energy()

atoms3.calc =  ORBCalculator(orbff, device=device)
e3=atoms3.get_potential_energy()


# print SZ error in meV
with open("SIZE_CONSISTENCY_MLIP_DATA", "a") as f:
    f.write(f"ORB-v3 {1000*(e1-e2-e3)}\n")
f.close()
