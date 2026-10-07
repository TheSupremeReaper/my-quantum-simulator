import numpy as np

from my_quantum_simulator import states


def test_prepare_init_state():
    ref_init_state = np.array([1, 0, 0, 0, 0, 0, 0, 0])

    init_state = states.prepare_init_state(3)

    np.testing.assert_allclose(init_state, ref_init_state, atol=1e-12)
