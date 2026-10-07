import numpy as np
from numpy.typing import NDArray


def sample_state(state_vector: NDArray, shots: int) -> dict:
    """
    Simulate the sampling for a given statevector

    Args:
        state_vector (NDArray): A statevector
        shots (int): The total number of samples to take.

    Returns:
        dict: Results of the sampling given as a dictionary. Keys are bit strings (ex : "0110") and values integers.
    """

    ### À compléter
    bit_strings = []
    counts = []
    ###

    return dict(zip(bit_strings, [int(count) for count in counts]))
