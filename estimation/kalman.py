import numpy as np

class KalmanFilter1D:
    def __init__(self, dt):
        self.dt = dt

        self.A = np.array([[1, dt],
                           [0, 1]])

        self.B = np.array([[0.5 * dt**2],
                           [dt]])

        self.H = np.array([[1, 0]])

        self.Q = np.diag([1e-6, 1e-4])
        self.R = np.array([[0.05**2]])

        self.P = np.eye(2)
        self.x = np.zeros((2, 1))

    def predict(self, acceleration):
        u = np.array([[acceleration]])
        self.x = self.A @ self.x + self.B @ u
        self.P = self.A @ self.P @ self.A.T + self.Q

    def update(self, z_meas):
        z = np.array([[z_meas]])

        S = self.H @ self.P @ self.H.T + self.R
        K = self.P @ self.H.T @ np.linalg.inv(S)

        self.x = self.x + K @ (z - self.H @ self.x)
        self.P = (np.eye(2) - K @ self.H) @ self.P

        return self.x
