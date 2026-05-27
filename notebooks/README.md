# Hybrid Quantum State Preparation via Classical Compression and Quantum Decompression

This repository provides a collection of numerical and quantum-circuit demonstrations for hybrid quantum state preparation (Hybrid-QSP). The framework combines classical signal transformations and sparsification techniques with quantum state preparation and inverse quantum reconstruction.

The main objective is to reduce the complexity of quantum state preparation by exploiting transform-domain sparsity. Signals are first compressed classically using reversible transformations such as the Fourier transform or Haar packet wavelet transform. Sparse transform-domain coefficients are then encoded into quantum amplitudes, followed by inverse quantum transformations to reconstruct the original signal approximately or exactly.

---

## Hybrid Quantum State Preparation Algorithm

Given a classical vector

\[ __x__= [x_0, x_1, \dots, x_{N-1}]^T \in \mathbb{R}^N,
\]

the goal is to approximately prepare the quantum state

\[
|\Phi\rangle
\approx
\sum_{k=0}^{N-1}
x_k |k\rangle.
\]

The workflow of the Hybrid-QSP framework is:

1. Apply a reversible classical transformation
   \[
   \mathbf{X}
   =
   \mathcal{U}_C \mathbf{x}.
   \]

2. If the transformed vector is not sufficiently sparse:
   - retain dominant coefficients,
   - apply thresholding or Top-k sparsification.

3. Normalize the sparse coefficient vector
   \[
   \mathbf{X}^r
   =
   \frac{
   \mathbf{X}^{(\tau)}
   }{
   \|
   \mathbf{X}^{(\tau)}
   \|_2
   }.
   \]

4. Prepare the compressed quantum state
   \[
   |\phi\rangle
   =
   \sum_{k=0}^{N-1}
   X_k^r |k\rangle.
   \]

5. Apply the inverse quantum transformation
   \[
   |\Phi\rangle
   =
   \mathcal{U}_Q^{-1}
   |\phi\rangle.
   \]

6. Compare the reconstructed quantum state with the normalized original signal using fidelity and trace-distance metrics.

In the absence of thresholding, the reconstruction becomes exact.

---

## Available Examples

| Example | Description |
|---|---|
| Multi-frequency signal | Exact sparse representation in the Fourier domain |
| Piecewise-constant signal | Exact sparse representation using Haar packet decomposition |
| Sinc signal | Approximate sparse reconstruction using Top-k thresholding |
| Single-Gaussian signal | Sparse approximation of smooth localized signals |
| Multi-Gaussian signal | Sparse representation of multi-peak structures |
| PPG signal | Hybrid quantum reconstruction of biomedical physiological signals |