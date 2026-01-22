import numpy as np
import matplotlib.pyplot as plt

# Parameters
u = 50
theta = 45
g = 9.8

theta = np.radians(theta)

T = 2 * u * np.sin(theta) / g
t = np.linspace(0, T, 100)

x = u * np.cos(theta) * t
y = u * np.sin(theta) * t - 0.5 * g * t**2

plt.plot(x, y)
plt.xlabel("Range (m)")
plt.ylabel("Height (m)")
plt.title("Projectile Motion (Analytical Solution)")
plt.show()
