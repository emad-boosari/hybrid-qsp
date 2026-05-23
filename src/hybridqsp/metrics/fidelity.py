import numpy as np


def state_fidelity(psi, phi):
    """
    Compute fidelity between two pure states.

    Parameters
    ----------
    psi : np.ndarray
        First state vector.
    phi : np.ndarray
        Second state vector.

    Returns
    -------
    float
        Fidelity value in [0, 1].
    """

    psi = np.asarray(psi, dtype=np.complex128)
    phi = np.asarray(phi, dtype=np.complex128)

    norm_psi = np.linalg.norm(psi)
    norm_phi = np.linalg.norm(phi)

    if norm_psi == 0 or norm_phi == 0:
        return np.nan

    psi = psi / norm_psi
    phi = phi / norm_phi

    fidelity = np.abs(np.vdot(psi, phi)) ** 2

    return float(np.clip(fidelity, 0.0, 1.0))