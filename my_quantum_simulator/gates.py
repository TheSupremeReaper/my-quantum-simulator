import numpy as np
from numpy.typing import NDArray

X_GATE = np.array([[0, 1], [1, 0]])
Y_GATE = np.array([[0, -1j], [1j, 0]])
Z_GATE = np.array([[1, 0], [0, -1]])
H_GATE = np.sqrt(0.5) * np.array([[1, 1], [1, -1]])


def build_ry_gate(angle: float) -> NDArray:
    """
    Builds the matrix of a Ry gate for a given angle.

    Args:
        angle (float): The angle of the rotation around the y axis.

    Returns:
        NDArray: Matrix representation of a Ry rotation.
    """

    ### À compléter
    ry_gate = None
    ###

    return ry_gate


def control(gate: NDArray) -> NDArray:
    """
    Convert a gate into a controlled gate. The control qubit is the index 0 qubit.

    Args:
        gate (NDArray): Array representation of a gate. Basis using little-endian.

    Returns:
        NDArray: Array representation of the controlled gate controlled by the 0th qubit. Basis using little-endian.
    """

    ### À compléter
    control_gate = None
    ###

    return control_gate


def reorder_qubits_gate(gate: NDArray, order: list[int]) -> NDArray:
    """
    Transforms the Array of a gate by changing the qubit order.
    Ex : [2,0,1] means qubit 0 goes to position 2, qubit 1 goes to position 0 and qubit 2 goes to 1.

    Args:
        gate (NDArray): Array representation of a gate. Basis using little-endian.
        order (list[int]): Order in which to place the qubits.

    Returns:
        NDArray: Array representation of the gate with qubits moved around.
    """

    order = np.array(order)
    number_of_qubits = int(np.log2(gate.shape[0]))
    assert np.all(np.sort(order) == np.arange(number_of_qubits))

    from_qubit_order = np.arange(number_of_qubits)
    to_qubit_order = order

    from_dim_index = number_of_qubits - 1 - from_qubit_order
    to_dim_index = number_of_qubits - 1 - to_qubit_order

    basis_order = np.arange(2**number_of_qubits)
    tensor_shape = (2,) * number_of_qubits

    ### À compléter
    basis_reorder = None
    ###
    reordered_gate = gate[basis_reorder, :][:, basis_reorder]

    return reordered_gate


def convert_to_more_qubits(gate: NDArray, number_of_qubits: int, apply_on_qubits: list[int]) -> NDArray:
    """
    Convert a gate to a higher number of qubits adding identity operator to additional qubits. Apply the gate given a set of qubits.

    Args:
        gate (NDArray): Array representation of a gate. Basis using little-endian.
        number_of_qubits (int): The total number to convert the gate to.
        apply_on_qubits (list[int]): On which qubits the original ate should be applied

    Returns:
        NDArray: Array representation of the gate with additional qubits.
    """

    gate_number_of_qubits = int(np.log2(gate.shape[0]))
    assert len(apply_on_qubits) == gate_number_of_qubits
    assert number_of_qubits > gate_number_of_qubits

    ### À compléter
    new_gate = None
    ###

    return new_gate


def compose_gates(gates: tuple[NDArray]) -> NDArray:
    """
    Computes the resulting matrix for gate composition.

    Args:
        gates (list[NDArray]): A list of gates given as Arrays.

    Returns:
        NDArray: The Array of the composed gate.
    """

    ### À compléter
    composition_gate = None
    ###

    return composition_gate
