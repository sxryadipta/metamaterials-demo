# ML Forward Model for Metamaterial Absorption (Demo)

This repository demonstrates a minimal **machine-learning-only**
forward design model that predicts absorption spectra from
metamaterial geometry parameters.

## Problem
Predict the absorption spectrum of a single-layer metamaterial absorber
from geometric parameters.

- Inputs: Patch length (L), width (W), substrate thickness (h)
- Output: Absorption spectrum (100 frequency points)

## Model
- Algorithm: Multi-output Random Forest Regression
- Learning type: Supervised
- Physics inside model: None (black-box learning)

## Dataset
- 20 samples (proof-of-concept)
- Synthetic data used as a placeholder for EM simulation outputs
  (e.g., COMSOL / HFSS)

## Run
```bash
pip install -r requirements.txt
python demo.py
