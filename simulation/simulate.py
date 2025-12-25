import numpy as np
from dynamics.equations import vertical_dynamics
from simulation.sensors import altimeter

def simulate_vertical_kf(pid, kf, z_ref, m, g, dt, T):
    steps = int(T / dt)

    state = np.array([0.0, 0.0])  # [height, velocity]

    time = []
    z_true_hist = []
    z_meas_hist = []
    z_est_hist = []

    for i in range(steps):
        t = i * dt
        z_true, z_dot = state

        # sensor
        z_meas = altimeter(z_true)

        # estimation
        z_hat = kf.update(z_meas)
        z_est = z_hat[0, 0]

        # control (uses estimated state)
        error = z_ref - z_est
        u = pid.update(error, dt)
        thrust = m * g + u

        #prediction
        acc = thrust / m - g
        kf.predict(acc)

        # physics update
        state_dot = vertical_dynamics(state, thrust)
        state = state + dt * state_dot

        # log
        time.append(t)
        z_true_hist.append(z_true)
        z_meas_hist.append(z_meas)
        z_est_hist.append(z_est)

    return {
        "time": np.array(time),
        "z_true": np.array(z_true_hist),
        "z_meas": np.array(z_meas_hist),
        "z_est": np.array(z_est_hist)
    }
