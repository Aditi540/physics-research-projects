import numpy as np
import matplotlib.pyplot as plt

# Parameters
u = 50
theta = 45
g = 9.8

theta = np.radians(theta)

# Time array
t = np.linspace(0, 10, 500)

# Analytical solution
x_analytical = u * np.cos(theta) * t
y_analytical = u * np.sin(theta) * t - 0.5 * g * t**2

# Numerical solution (Euler Method)
dt = 0.02
vx = u * np.cos(theta)
vy = u * np.sin(theta)

x, y = 0, 0
xs, ys = [], []

while y >= 0:
    xs.append(x)
    ys.append(y)
    x += vx * dt
    y += vy * dt
    vy -= g * dt

# Plot comparison
plt.plot(x_analytical, y_analytical, label="Analytical Solution")
plt.plot(xs, ys, '--', label="Euler Numerical Solution")

plt.xlabel("Range (m)")
plt.ylabel("Height (m)")
plt.title("Projectile Motion: Analytical vs Numerical Comparison")
plt.legend()
plt.grid()
plt.show()
