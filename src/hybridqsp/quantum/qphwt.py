from qibo import Circuit, gates


def qhw(circuit, n, offset=0):
    """
    Forward Qibo-compatible quantum Haar-wavelet block.
    """

    if n < 1:
        raise ValueError(
            "Number of qubits must be positive."
        )

    # Hadamard on last active qubit
    circuit.add(
        gates.H(offset + n - 1)
    )

    # Reverse SWAP propagation
    for i in reversed(range(n - 1)):

        circuit.add(
            gates.SWAP(
                offset + i + 1,
                offset + i
            )
        )


def inverse_qhw(circuit, n, offset=0):
    """
    Inverse Qibo-compatible quantum Haar-wavelet block.
    """

    if n < 1:
        raise ValueError(
            "Number of qubits must be positive."
        )

    # Forward SWAP propagation
    for i in range(n - 1):

        circuit.add(
            gates.SWAP(
                offset + i + 1,
                offset + i
            )
        )

    # Final Hadamard
    circuit.add(
        gates.H(offset + n - 1)
    )


def build_qphwt_circuit(n, level):
    """
    Construct forward QPHWT circuit.
    """

    if not (1 <= level < n):
        raise ValueError(
            "Require 1 <= level < n."
        )

    circuit = Circuit(n)

    for current_level in range(level):

        active_qubits = n - current_level

        qhw(
            circuit=circuit,
            n=active_qubits,
            offset=0
        )

    return circuit


def build_inverse_qphwt_circuit(n, level):
    """
    Construct inverse QPHWT circuit.
    """

    if not (1 <= level < n):
        raise ValueError(
            "Require 1 <= level < n."
        )

    circuit = Circuit(n)

    for current_level in range(level):

        active_qubits = n - current_level

        inverse_qhw(
            circuit=circuit,
            n=active_qubits,
            offset=0
        )

    return circuit