import numpy as np

from hybridqsp.transforms import (
    haar_packet_transform,
    inverse_haar_packet_transform
)

from hybridqsp.thresholding import (
    magnitude_threshold
)

from hybridqsp.metrics import (
    trace_distance,
    state_fidelity
)


def search_sparse_haar_representations(
    signal,
    tolerance=0.02,
    threshold_ratios=None
):
    """
    Search for sparse Haar-packet representations
    that satisfy a reconstruction-error tolerance.

    Parameters
    ----------
    signal : np.ndarray
        Input signal.

    tolerance : float, optional
        Maximum allowed trace distance.

    threshold_ratios : list, optional
        Relative threshold values with respect to
        max(abs(coefficients)).

    Returns
    -------
    list
        Accepted sparse configurations.
    """

    signal = np.asarray(signal, dtype=float)

    N = len(signal)

    # Maximum allowed decomposition level
    max_level = int(np.log2(N))
    min_level = max(1, max_level // 2)

    levels = list(range(min_level, max_level + 1))
    
    if threshold_ratios is None:

        threshold_ratios = [
            0.001,
            0.002,
            0.005,
            0.01,
            0.02,
            0.05,
            0.1
        ]

    accepted_results = []

    for level in levels:

        # Haar packet decomposition
        coeffs = haar_packet_transform(
            signal,
            level=level
        )

        # Maximum coefficient magnitude
        max_coeff = np.max(np.abs(coeffs))

        for ratio in threshold_ratios:

            threshold = ratio * max_coeff

            # Threshold coefficients
            coeffs_sparse = magnitude_threshold(
                coeffs,
                threshold=threshold
            )

            # Reconstruction
            reconstructed_signal = (
                inverse_haar_packet_transform(
                    coeffs_sparse,
                    level=level
                )
            )

            # Metrics
            D = trace_distance(
                signal,
                reconstructed_signal
            )

            F = state_fidelity(
                signal,
                reconstructed_signal
            )

            # Sparsity
            nonzero = np.count_nonzero(
                coeffs_sparse
            )

            sparsity_ratio = (
                nonzero / len(coeffs_sparse)
            )

            # Keep acceptable results
            if D < tolerance:

                result = {
                    "level": level,
                    "threshold": threshold,
                    "nonzero": nonzero,
                    "sparsity_ratio": sparsity_ratio,
                    "trace_distance": D,
                    "fidelity": F
                }

                accepted_results.append(result)

                print(
                    f"Level={level} | "
                    f"Threshold={threshold:.3e} | "
                    f"Nonzero={nonzero} | "
                    f"Sparsity={sparsity_ratio:.3f} | "
                    f"Trace Distance={D:.6e} | "
                    f"Fidelity={F:.6f}"
                )

    return accepted_results