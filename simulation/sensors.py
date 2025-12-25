import numpy as np

def altimeter(true_z, sigma=0.02):
    """
    Simulate an altimeter with noise
    """
    noise = np.random.normal(0.0, sigma)
    return true_z + noise
