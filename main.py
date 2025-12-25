import matplotlib.pyplot as plt
from control.pid import PID
from simulation.simulate import simulate_vertical_pid
from dynamics.params import m, g

pid = PID(kp=15.0, ki=2.0, kd=5.0)
z_ref = 1.0  # target height (meters)

history = simulate_vertical_pid(pid, z_ref, m, g)

z = history[:, 0]

plt.figure()
plt.plot(z)
plt.axhline(z_ref, linestyle="--", color="r")
plt.xlabel("Time step")
plt.ylabel("Height (m)")
plt.title("Altitude Control with PID")
plt.savefig("plots/phase2.png", dpi=150, bbox_inches="tight")
plt.show()
