import matplotlib.pyplot as plt
from simulation.simulate import simulate_vertical
from dynamics.params import m, g

thrust = m * g * 1.2  # hover + extra
history = simulate_vertical(thrust)

z = history[:, 0]

plt.plot(z)
plt.xlabel("Time step")
plt.ylabel("Height (m)")
plt.title("Vertical Motion of Quadcopter")
plt.show()
