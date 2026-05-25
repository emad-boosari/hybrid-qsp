from qibo import Circuit, gates


def qhw(circuit, n, offset=0):
    """
    Apply a quantum Haar-wavelet block
    on n qubits starting from `offset`.

    Parameters
    ----------
    circuit : qibo.Circuit
        Circuit to modify.

    n : int
        Number of active qubits.

    offset : int, optional
        Starting qubit index.
    """

    if n < 1:
        raise ValueError(
            "Number of qubits must be positive."
        )

    circuit.add(gates.H(offset))

    for i in range(n - 1):
        circuit.add(
            gates.SWAP(
                offset + i,
                offset + i + 1
            )
        )


def build_qphwt_circuit(n, level):
    """
    Construct a Quantum Packet Haar Wavelet
    Transform (QPHWT) circuit.

    Parameters
    ----------
    n : int
        Total number of qubits.

    level : int
        Number of decomposition levels.

    Returns
    -------
    qibo.Circuit
        Constructed QPHWT circuit.
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


def inverse_qhw(circuit, n, offset=0):
    """
    Apply the inverse quantum Haar-wavelet
    block on n qubits starting from `offset`.

    Parameters
    ----------
    circuit : qibo.Circuit
        Circuit to modify.

    n : int
        Number of active qubits.

    offset : int, optional
        Starting qubit index.
    """

    if n < 1:
        raise ValueError(
            "Number of qubits must be positive."
        )

    # Reverse SWAP order
    for i in reversed(range(n - 1)):

        circuit.add(
            gates.SWAP(
                offset + i,
                offset + i + 1
            )
        )

    # Hadamard inverse
    circuit.add(gates.H(offset))


def build_inverse_qphwt_circuit(n, level):
    """
    Construct the inverse Quantum Packet
    Haar Wavelet Transform (QPHWT) circuit.

    Parameters
    ----------
    n : int
        Total number of qubits.

    level : int
        Number of decomposition levels.

    Returns
    -------
    qibo.Circuit
        Constructed inverse QPHWT circuit.
    """

    if not (1 <= level < n):
        raise ValueError(
            "Require 1 <= level < n."
        )

    circuit = Circuit(n)

    # Reverse decomposition order
    for current_level in reversed(range(level)):

        active_qubits = n - current_level

        inverse_qhw(
            circuit=circuit,
            n=active_qubits,
            offset=0
        )

    return circuit