import numpy as np
import matplotlib.pyplot as plt

# Parameters
u = 50
theta = 45
g = 9.8

theta = np.radians(theta)

# Initial conditions
vx = u * np.cos(theta)
vy = u * np.sin(theta)

dt = 0.01
x, y = 0, 0
xs, ys = [], []

# Euler Method loop
while y >= 0:
    xs.append(x)
    ys.append(y)

    x += vx * dt
    y += vy * dt

    vy -= g * dt   # gravity affects velocity

plt.plot(xs, ys)
plt.xlabel("Range (m)")
plt.ylabel("Height (m)")
plt.title("Projectile Motion (Euler Numerical Method)")
plt.show()
