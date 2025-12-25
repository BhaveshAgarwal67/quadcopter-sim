import numpy as np
from dynamics.equations import vertical_dynamics

def simulate_vertical_pid(pid, z_ref, m, g, dt=0.01, T=5.0):
    steps = int(T / dt)
    state = np.array([0.0, 0.0])  # [height, velocity]

    history = []

    for _ in range(steps):
        z, z_dot = state
        error = z_ref - z

        u = pid.update(error, dt)
        thrust = m * g + u  # hover thrust + change

        state_dot = vertical_dynamics(state, thrust)
        state = state + dt * state_dot

        history.append(state.copy())

    return np.array(history)
