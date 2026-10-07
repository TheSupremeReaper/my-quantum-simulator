import numpy as np

from my_quantum_simulator import gates, measure, states


def test_sample_state():
    h_gate = np.sqrt(0.5) * np.array([[1, 1], [1, -1]])
    s_gate = np.array([[1, 0], [0, 1j]])
    c0x1_gate = np.array([[1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0]])
    ih_gate = gates.convert_to_more_qubits(h_gate, 2, [0])
    is_gate = gates.convert_to_more_qubits(s_gate, 2, [0])

    bell_circuit = c0x1_gate @ is_gate @ ih_gate

    init_state = states.prepare_init_state(2)

    final_state = bell_circuit @ init_state

    counts = measure.sample_state(final_state, 1000)

    assert "01" not in counts
    assert "10" not in counts

    values = list(counts.values())

    assert np.round(values[0] / values[1]) == 1


def test_sample_state_2():
    h_gate = np.sqrt(0.5) * np.array([[1, 1], [1, -1]])
    t_gate = np.array([[1, 0], [0, (1 + 1j) / np.sqrt(2)]])
    c0x1_gate = np.array([[1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0]])
    ih_gate = gates.convert_to_more_qubits(h_gate, 2, [0])
    is_gate = gates.convert_to_more_qubits(t_gate, 2, [0])

    bell_circuit = c0x1_gate @ is_gate @ ih_gate

    init_state = states.prepare_init_state(2)

    final_state = bell_circuit @ init_state

    counts = measure.sample_state(final_state, 1000)

    assert "01" not in counts
    assert "10" not in counts

    values = list(counts.values())

    assert np.round(values[0] / values[1]) == 1
