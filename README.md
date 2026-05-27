# Hybrid Quantum State Preparation via Classical Compression

A modular research framework for hybrid quantum state preparation using classical transform-domain compression techniques such as Fourier and Haar wavelet sparsification.

---

## Overview

Quantum state preparation is one of the central bottlenecks in many quantum algorithms.  
This project explores hybrid quantum-classical strategies in which classical compression methods are applied prior to quantum encoding in order to reduce quantum resource requirements while preserving reconstruction fidelity.

The framework currently includes:

- Classical Fourier and Haar-based transforms
- Sparse coefficient thresholding methods
- Fidelity and trace-distance evaluation metrics
- Quantum Packet Haar Wavelet Transform (QPHWT) circuits
- Qibo-based quantum circuit implementations
- Reproducible notebook demonstrations

---

## Repository Structure

```text
hybrid-qsp/
│
├── src/
│   └── hybridqsp/
│       ├── transforms/
│       │   ├── __init__.py
│       │   ├── fourier.py
│       │   └── haar.py
│       │
│       ├── thresholding/
│       │   ├── __init__.py
│       │   └── threshold.py
│       │
│       ├── metrics/
│       │   ├── __init__.py
│       │   └── distance.py
│       │
│       ├── quantum/
│       │   ├── __init__.py
│       │   └── qphwt.py
│       │
│       ├── analysis/
│       │   ├── __init__.py
│       │   └── haar_sparsity_search.py
│       │
│       └── __init__.py
│
├── notebooks/
│
├── figures/
│
├── datasets/
│
├── LICENSE
│
├── requirements.txt
│
└── README.md
```

---

## Current Features

### Classical Transforms

- Unitary Discrete Fourier Transform (DFT)
- Inverse DFT
- Haar transform
- Inverse Haar transform
- Haar packet wavelet transform

### Thresholding Methods

- Top-k coefficient thresholding
- Magnitude-based thresholding

### Metrics

- State fidelity
- Trace distance

### Quantum Components

- Quantum Packet Haar Wavelet Transform (QPHWT)
- Qibo-based circuit implementations

---

## Example Workflow

```python
from hybridqsp.transforms import dft, idft
from hybridqsp.thresholding import top_k_threshold
from hybridqsp.metrics import (
    state_fidelity,
    trace_distance
)

X = dft(signal)

X_sparse = top_k_threshold(X, k=8)

signal_rec = idft(X_sparse)

F = state_fidelity(signal, signal_rec)
D = trace_distance(signal, signal_rec)
```

---

## Notebook Demonstrations

The `notebooks/` directory contains reproducible examples demonstrating:

- Fourier-domain sparsification
- Haar-wavelet compression
- Signal reconstruction
- Sparse quantum representations
- Biomedical signal examples

---

## Current Status

This repository is under active development alongside the associated research manuscript.

---

## License

This project is released under the MIT License.

## Associated Paper

This repository accompanies the following research manuscript:

**Hybrid Quantum State Preparation via Classical Compression and Quantum Decompression**  
https://arxiv.org/abs/2512.01798
