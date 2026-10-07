import numpy as np

from my_quantum_simulator import gates


def assert_gates_equivalent(gate1, gate2):
    prod = gate1 @ gate2.T.conj() @ gate1.T.conj() @ gate2

    np.testing.assert_allclose(prod, np.eye(prod.shape[0]), atol=1e-12)


# class TestMQS(unittest.TestCase):
def test_build_ry_gate():
    y_gate = np.array([[0, -1j], [1j, 0]])

    new_y_gate = gates.build_ry_gate(np.pi)

    assert_gates_equivalent(new_y_gate, y_gate)


def test_control():
    x_gate = np.array([[0, 1], [1, 0]])
    ref_cx_gate = np.array([[1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0]])

    cx_gate = gates.control(x_gate)

    assert_gates_equivalent(cx_gate, ref_cx_gate)


def test_control_2():
    x_gate = np.array([[0, 1], [1, 0]])
    ref_ccx_gate = np.array(
        [
            [1, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
        ]
    )

    ccx_gate = gates.control(gates.control(x_gate))

    assert_gates_equivalent(ccx_gate, ref_ccx_gate)


def test_compose_gates():

    XHZ_gate = gates.compose_gates((gates.Z_GATE, gates.H_GATE, gates.X_GATE))

    assert_gates_equivalent(XHZ_gate, gates.H_GATE)


def test_reorder_qubits_gate():
    ref_c0x1_gate = np.array([[1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0]])

    c1x0_gate = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])

    c0x1_gate = gates.reorder_qubits_gate(c1x0_gate, [1, 0])

    assert_gates_equivalent(c0x1_gate, ref_c0x1_gate)

    ref_i0c1x2_gate = np.kron(
        np.array([[1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0]]), np.array([[1, 0], [0, 1]])
    )

    c0x1i2_gate = np.kron(
        np.array([[1, 0], [0, 1]]), np.array([[1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0]])
    )

    i0c1x2 = gates.reorder_qubits_gate(c0x1i2_gate, [1, 2, 0])

    assert_gates_equivalent(i0c1x2, ref_i0c1x2_gate)

    assert_gates_equivalent(
        gates.reorder_qubits_gate(c0x1i2_gate, [0, 2, 1]), gates.reorder_qubits_gate(ref_i0c1x2_gate, [1, 0, 2])
    )


def test_reorder_qubits_gate_random():

    num_qubits = 3

    random_matrix = np.random.random((2**num_qubits, 2**num_qubits)) + 1j * np.random.random(
        (2**num_qubits, 2**num_qubits)
    )
    random_hermitian = random_matrix + random_matrix.conj().T

    eig_values, eig_vectors = np.linalg.eigh(random_hermitian)

    random_unitary = np.einsum("p,ip,jp->ij", np.exp(1j * eig_values), eig_vectors, eig_vectors.conj())

    qubit_order_1 = [0, 2, 1]
    dim_order_1 = [0, 1, 4, 5, 2, 3, 6, 7]

    reorder_unitary_1 = random_unitary[dim_order_1, :][:, dim_order_1]

    assert_gates_equivalent(reorder_unitary_1, gates.reorder_qubits_gate(random_unitary, qubit_order_1))

    qubit_order_2 = [1, 0, 2]
    dim_order_2 = [0, 2, 1, 3, 4, 6, 5, 7]

    reorder_unitary_2 = random_unitary[dim_order_2, :][:, dim_order_2]

    assert_gates_equivalent(reorder_unitary_2, gates.reorder_qubits_gate(random_unitary, qubit_order_2))

    qubit_order_3 = [1, 2, 0]
    dim_order_3 = [0, 4, 1, 5, 2, 6, 3, 7]

    reorder_unitary_3 = random_unitary[dim_order_3, :][:, dim_order_3]

    assert_gates_equivalent(reorder_unitary_3, gates.reorder_qubits_gate(random_unitary, qubit_order_3))


def test_convert_to_more_qubits():
    ref_c0x1_gate = np.array([[1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0]])

    ref_c2x0 = np.array(
        [
            [1, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 1, 0],
        ]
    )

    ref_c2x1 = np.array(
        [
            [1, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
        ]
    )

    c2x0 = gates.convert_to_more_qubits(ref_c0x1_gate, 3, [2, 0])

    np.testing.assert_allclose(c2x0, ref_c2x0, atol=1e-12)

    c2x1 = gates.convert_to_more_qubits(ref_c0x1_gate, 3, [2, 1])

    np.testing.assert_allclose(c2x1, ref_c2x1, atol=1e-12)


def test_c0x1c2():
    ref_c0x1c2_gate = np.array(
        [
            [1, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
        ]
    )

    x_gate = np.array([[0, 1], [1, 0]])
    c0x1_gate = gates.control(x_gate)
    c0c1x2_gate = gates.control(c0x1_gate)

    c0x1c2_gate = gates.reorder_qubits_gate(c0c1x2_gate, [0, 2, 1])

    assert_gates_equivalent(c0x1c2_gate, ref_c0x1c2_gate)


def test_c0x2():
    ref_c0x2_gate = np.array(
        [
            [1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
        ]
    )

    x_gate = np.array([[0, 1], [1, 0]])
    c0x1_gate = gates.control(x_gate)

    c0x2_gate = gates.convert_to_more_qubits(c0x1_gate, 3, [0, 2])

    assert_gates_equivalent(c0x2_gate, ref_c0x2_gate)
