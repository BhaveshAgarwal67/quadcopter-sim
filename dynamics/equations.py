import numpy as np
from dynamics.params import m, g

def vertical_dynamics(state, thrust):
    z, zdot = state
    zddot = thrust / m - g
    return np.array([zdot, zddot])