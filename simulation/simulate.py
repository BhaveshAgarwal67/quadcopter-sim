import numpy as np
from dynamics.equations import vertical_dynamics

def simulate_vertical(thrust, dt=0.01, T=5.0):
    steps = int(T / dt)
    state = np.array([0.0, 0.0])  # initial height and velocity

    history = []

    for _ in range(steps):
        state_dot = vertical_dynamics(state, thrust)
        state = state + dt * state_dot
        history.append(state.copy())

    return np.array(history)