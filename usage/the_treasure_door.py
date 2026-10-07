# %% imports and definitions
from my_quantum_simulator import gates, measure, states

# %% Circuit construction

CX_GATE = gates.control(gates.X_GATE)
SWAP_GATE = gates.compose_gates(
    (
        CX_GATE,
        gates.reorder_qubits_gate(CX_GATE, [1, 0]),
        CX_GATE,
    )
)

setup_circuit = gates.compose_gates(
    (
        gates.convert_to_more_qubits(CX_GATE, 3, [0, 1]),
        gates.convert_to_more_qubits(gates.H_GATE, 3, [2]),
        gates.convert_to_more_qubits(gates.H_GATE, 3, [0]),
    )
)
lying_circuit = gates.compose_gates(
    (
        gates.convert_to_more_qubits(gates.X_GATE, 3, [2]),
        gates.convert_to_more_qubits(CX_GATE, 3, [2, 0]),
        gates.convert_to_more_qubits(gates.X_GATE, 3, [2]),
        gates.convert_to_more_qubits(CX_GATE, 3, [2, 1]),
    )
)
do_not_circuit = gates.compose_gates(
    (
        gates.convert_to_more_qubits(gates.X_GATE, 3, [1]),
        gates.convert_to_more_qubits(gates.X_GATE, 3, [0]),
        gates.convert_to_more_qubits(SWAP_GATE, 3, [0, 1]),
    )
)

the_treasure_door_circuit = gates.compose_gates(
    (
        lying_circuit,
        do_not_circuit,
        lying_circuit,
        setup_circuit,
    )
)

# %% Circuit simulation

init_state = states.prepare_init_state(3)

final_state = states.apply_gate_on_state(the_treasure_door_circuit, init_state)

# %% Measurement simulation

counts = measure.sample_state(final_state, shots=1000)

print(counts)

# %%
