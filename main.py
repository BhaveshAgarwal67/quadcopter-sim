import matplotlib.pyplot as plt

from control.pid import PID
from estimation.kalman import KalmanFilter1D
from simulation.simulate import simulate_vertical_kf
from dynamics.params import m, g

# parameters
dt = 0.01
T = 4.0
z_ref = 1.0

pid = PID(kp=15.0, ki=2.0, kd=5.0)
kf = KalmanFilter1D(dt)

history = simulate_vertical_kf(
    pid=pid,
    kf=kf,
    z_ref=z_ref,
    m=m,
    g=g,
    dt=dt,
    T=T
)

time = history["time"]
z_true = history["z_true"]
z_meas = history["z_meas"]
z_est = history["z_est"]

plt.figure(figsize=(8, 5))
plt.plot(time, z_true, label="True altitude", linewidth=2)
plt.plot(time, z_meas, label="Measured altitude", linewidth=1, alpha=0.4)
plt.plot(time, z_est, label="Estimated altitude", linewidth=2)
plt.axhline(z_ref, linestyle="--", color="r", label="Reference")

plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.title("Altitude Estimation with Kalman Filter (Phase 3)")
plt.legend()
plt.grid(True)

plt.savefig("plots/phase3.png", dpi=300, bbox_inches="tight")
plt.show()
