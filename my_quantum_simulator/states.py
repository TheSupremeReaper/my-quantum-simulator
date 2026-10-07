import numpy as np
from numpy.typing import NDArray


def prepare_init_state(number_of_qubits: int) -> NDArray:
    """
    Prepare the initial statevector (all qubits in state zero)

    Args:
        number_of_qubits (int): The number of qubits.

    Returns:
        NDArray: The statevector
    """

    ### À compléter
    init_state = None
    ###

    return init_state


def apply_gate_on_state(gate: NDArray, state: NDArray) -> NDArray:
    """
    Apply gate to a state and return the resulting state.

    Args:
        gate (NDArray): A gate or a circuit as a matric
        state (NDArray): A state as a vector

    Returns:
        NDArray: The final state as a vector
    """

    ### À compléter
    final_state = None
    ###

    return final_state
