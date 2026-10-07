# %% Imports and Definitions

from my_quantum_simulator import gates, measure, states

# %% Circuit construction

CX_GATE = gates.control(gates.X_GATE)

bell_circuit = gates.compose_gates(
    (
        gates.convert_to_more_qubits(gates.H_GATE, 2, [0]),
        CX_GATE,
    )
)

# %% Circuit Simulation

init_state = states.prepare_init_state(2)

final_state = states.apply_gate_on_state(bell_circuit, init_state)

# %% Measurement Simulation

counts = measure.sample_state(final_state, shots=1000)

print(counts)

# %%
