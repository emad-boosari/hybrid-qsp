import numpy as np

from .fidelity import state_fidelity


def trace_distance(psi, phi):
    """
    Compute trace distance between two pure states.

    Parameters
    ----------
    psi : np.ndarray
        First state vector.
    phi : np.ndarray
        Second state vector.

    Returns
    -------
    float
        Trace distance.
    """

    fidelity = state_fidelity(psi, phi)

    if np.isnan(fidelity):
        return np.nan

    return float(np.sqrt(1.0 - fidelity))