import numpy as np
import matplotlib.pyplot as plt
from ase.io import read
from copy import deepcopy
from mattersim.forcefield import MatterSimCalculator

device="cpu" 

atoms1 = read("POSCAR_far")
atoms2 = read("POSCAR_graphene")
atoms3 = read("POSCAR_co2")


atoms1.calc = MatterSimCalculator(load_path="MatterSim-v1.0.0-5M.pth", device=device)
e1=atoms1.get_potential_energy()

atoms2.calc = MatterSimCalculator(load_path="MatterSim-v1.0.0-5M.pth", device=device)
e2=atoms2.get_potential_energy()

atoms3.calc = MatterSimCalculator(load_path="MatterSim-v1.0.0-5M.pth", device=device)
e3=atoms3.get_potential_energy()


# print SZ error in meV
with open("SIZE_CONSISTENCY_MLIP_DATA", "a") as f:
    f.write(f"MatterSim {1000*(e1-e2-e3)}\n")
f.close()
