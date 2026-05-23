import numpy as np


def magnitude_threshold(x, threshold):
    """
    Remove coefficients whose magnitude
    is below a given threshold.

    Parameters
    ----------
    x : np.ndarray
        Input vector.
    threshold : float
        Magnitude threshold.

    Returns
    -------
    np.ndarray
        Thresholded vector.
    """

    x = np.asarray(x)

    y = x.copy()

    y[np.abs(y) < threshold] = 0

    return y