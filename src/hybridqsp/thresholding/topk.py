import numpy as np


def top_k_threshold(x, k):
    """
    Keep the k largest-magnitude coefficients
    and set all others to zero.

    Parameters
    ----------
    x : np.ndarray
        Input vector.
    k : int
        Number of coefficients to keep.

    Returns
    -------
    np.ndarray
        Thresholded vector.
    """

    x = np.asarray(x)

    if k <= 0:
        return np.zeros_like(x)

    if k >= len(x):
        return x.copy()

    y = x.copy()

    indices = np.argsort(np.abs(y))

    remove_indices = indices[:-k]

    y[remove_indices] = 0

    return y