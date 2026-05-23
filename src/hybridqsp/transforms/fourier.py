import numpy as np


def dft(x):
    """
    Compute the unitary Discrete Fourier Transform (DFT).

    Parameters
    ----------
    x : np.ndarray
        Input 1D signal.

    Returns
    -------
    np.ndarray
        Fourier-transformed signal.
    """

    x = np.asarray(x, dtype=np.complex128)

    N = x.shape[0]

    n = np.arange(N)
    k = n.reshape((N, 1))

    omega = (
        np.exp(-2j * np.pi * k * n / N)
        / np.sqrt(N)
    )

    return omega @ x


def idft(x):
    """
    Compute the inverse unitary Discrete Fourier Transform (IDFT).

    Parameters
    ----------
    x : np.ndarray
        Fourier-domain signal.

    Returns
    -------
    np.ndarray
        Reconstructed signal.
    """

    x = np.asarray(x, dtype=np.complex128)

    N = x.shape[0]

    n = np.arange(N)
    k = n.reshape((N, 1))

    omega = (
        np.exp(+2j * np.pi * k * n / N)
        / np.sqrt(N)
    )

    return omega @ x