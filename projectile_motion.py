import numpy as np
import matplotlib.pyplot as plt

# Given values
u = 20              # initial velocity (m/s)
theta = 45          # angle in degrees
g = 9.8             # gravity (m/s^2)

# Convert angle to radians
theta_rad = np.radians(theta)

# Time of flight
T = (2 * u * np.sin(theta_rad)) / g

# Time array
t = np.linspace(0, T, 100)

# Equations of motion
x = u * np.cos(theta_rad) * t
y = u * np.sin(theta_rad) * t - 0.5 * g * t**2

# Plotting
plt.plot(x, y)
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.title("Projectile Motion Simulation")
plt.grid(True)
plt.show()
