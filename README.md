# Supplementary Data: *Interaction Strength of Carbon Dioxide on Graphene from Periodic Quantum Diffusion Monte Carlo*

This repository contains supplementary data supporting the findings of the publication:

**Della Pia F., Kler-Young G., Zen A., Berger F., Alfè D., Michaelides A.**  
*"Interaction strength of carbon dioxide on graphene from periodic quantum diffusion Monte Carlo"*

---

## 📁 Repository Structure

### `DATA/`
Contains input and output files used for DFT and DMC calculations.

Subdirectories include:
- `CO2_RANDOM_ADSORPTION_CONFIGURATIONS` – Tests on randomly sampled CO2 adsorption geometries
- `DFT_BINDING_CURVES` – input/output DFT-calculated binding curves
- `DFT_KPOINT_CONVERGENCE` – k-point convergence data for DFT
- `DFT_WATER_ON_GRAPHENE` – DFT data for water--graphene 
- `DMC_BINDING_CURVE` – Diffusion Monte Carlo binding energy curve
- `DMC_TWISTS` – Diffusion Monte Carlo tests with TABC
- `DMC_CASINO_INPUT_OUTPUT` – Input/output files for CASINO DMC calculations
- `DMC_MPC_vs_EWALD` – Data for comparison between MPC and Ewald DMC estimates
- `DMC_TIME_STEP_ERROR` – Data for the time step error analysis in DMC
- `MLFF_BINDING_CURVES` – Binding curves for co2 on graphene with machine learning potentials (and script to compute them with ASE) 
- `MLFF_WATER_ON_GRAPHENE_BINDING_CURVES` – Binding curves with machine learning potentials for water on graphene
- `vdwDF2_ADSORPTION_GEOMETRY` – Test on interaction energy computed on vdW-DF2 relaxed geometry
- `MLFF_SIZE_CONSISTENCY` – Test on SC error with MLFFs

---

### `PLOT_FOR_MAIN/`
Jupyter notebook to reproduce the main figures from the manuscript.

### `PLOT_FOR_SI/`
Jupyter notebook to reproduce the figures included in the Supporting Information (SI).

---

## 🧪 Citation

If you use this data or code, please cite the corresponding paper:

> Della Pia F, Kler-Young G, Zen A, Berger F, Alfè D, Michaelides A.  
> *Interaction strength of carbon dioxide on graphene from periodic quantum diffusion Monte Carlo*

---
