import numpy as np


def haar_transform(x):
    """
    One-level orthonormal Haar transform.
    """

    x = np.asarray(x, dtype=float)

    N = len(x)

    if N % 2 != 0:
        raise ValueError(
            "Signal length must be even."
        )

    x = x.reshape(-1, 2)

    avg = (x[:, 0] + x[:, 1]) / np.sqrt(2)
    diff = (x[:, 0] - x[:, 1]) / np.sqrt(2)

    return np.hstack([avg, diff])


def inverse_haar_transform(x):
    """
    One-level inverse Haar transform.
    """

    x = np.asarray(x, dtype=float)

    N = len(x)

    if N % 2 != 0:
        raise ValueError(
            "Signal length must be even."
        )

    half = N // 2

    avg = x[:half]
    diff = x[half:]

    a0 = (avg + diff) / np.sqrt(2)
    a1 = (avg - diff) / np.sqrt(2)

    return np.vstack([a0, a1]).T.reshape(-1)


def haar_packet_transform(x, level):
    """
    Hierarchical Haar packet transform.
    """

    x = np.asarray(x, dtype=float)

    N = len(x)

    if N % (2 ** level) != 0:
        raise ValueError(
            "Signal length must be divisible by 2**level."
        )

    y = x.copy()

    for current_level in range(1, level + 1):

        segment_length = N // (2 ** (current_level - 1))

        for start in range(0, N, segment_length):

            segment = y[start:start + segment_length]

            y[start:start + segment_length] = (
                haar_transform(segment)
            )

    return y


def inverse_haar_packet_transform(x, level):
    """
    Inverse hierarchical Haar packet transform.
    """

    x = np.asarray(x, dtype=float)

    N = len(x)

    if N % (2 ** level) != 0:
        raise ValueError(
            "Signal length must be divisible by 2**level."
        )

    y = x.copy()

    for current_level in reversed(range(1, level + 1)):

        segment_length = N // (2 ** (current_level - 1))

        for start in range(0, N, segment_length):

            segment = y[start:start + segment_length]

            y[start:start + segment_length] = (
                inverse_haar_transform(segment)
            )

    return y