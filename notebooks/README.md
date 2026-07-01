# Hybrid Quantum State Preparation via Classical Compression and Quantum Decompression

This repository provides a collection of numerical and quantum-circuit demonstrations for hybrid quantum state preparation (Hybrid-QSP). The framework combines classical signal transformations and sparsification techniques with quantum state preparation and inverse quantum reconstruction.

The main objective is to reduce the complexity of quantum state preparation by exploiting transform-domain sparsity. Signals are first compressed classically using reversible transformations such as the Fourier transform or Haar packet wavelet transform. Sparse transform-domain coefficients are then encoded into quantum amplitudes, followed by inverse quantum transformations to reconstruct the original signal approximately or exactly.

---

## Hybrid Quantum State Preparation Algorithm

Given a classical vector

$$ \vec{x}= [x_0, x_1, \dots, x_{N-1}]^T \in \mathbb{R}^N, $$


the goal is to approximately prepare the quantum state

$$ |\Phi\rangle \approx \sum_{k=0}^{N-1} x_k |k\rangle. $$

The workflow of the Hybrid-QSP framework is:

1. Apply a reversible classical transformation to the input signal.

2. Check whether the transformed coefficients are sufficiently sparse.

3. If necessary, apply thresholding or Top-k sparsification to retain only the dominant coefficients.

4. Normalize the remaining transform-domain coefficients.

5. Prepare the normalized sparse vector as a quantum state.

6. Apply the inverse quantum transformation to reconstruct the signal.

7. Compare the reconstructed state with the normalized original signal using fidelity and trace-distance metrics.

In the absence of thresholding, the reconstruction becomes exact.

---
