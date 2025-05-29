import numpy as np
import matplotlib.pyplot as plt
from ase.io import read
from copy import deepcopy
from fairchem.core import FAIRChemCalculator



atoms1 = read("POSCAR_far")
atoms2 = read("POSCAR_graphene")
atoms3 = read("POSCAR_co2")


atoms1.calc = FAIRChemCalculator(hf_hub_filename="uma_sm.pt", device="cuda", task_name="omc")
e1=atoms1.get_potential_energy()

atoms2.calc = FAIRChemCalculator(hf_hub_filename="uma_sm.pt", device="cuda", task_name="omc")
e2=atoms2.get_potential_energy()

atoms3.calc = FAIRChemCalculator(hf_hub_filename="uma_sm.pt", device="cuda", task_name="omc")
e3=atoms3.get_potential_energy()



# print SZ error in meV
with open("SIZE_CONSISTENCY_MLIP_DATA", "a") as f:
    f.write(f"UMA-OMC {1000*(e1-e2-e3)}\n")
f.close()
