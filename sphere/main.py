import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def simulate_sphere_division(steps, u_steps, v_steps):
    radius = 1.0
    x, y, z = [], [], []

    for step in range(steps + 1):
        compression_factor = 1.0 - step / steps * 0.8

        for u in range(u_steps):
            for v in range(v_steps):
                u_angle = u / u_steps * 2 * np.pi
                v_angle = v / v_steps * np.pi
                z_compression = (np.cos(v_angle) *
                                 compression_factor + 1) * 0.5

                x.append(radius * np.sin(v_angle) * np.cos(u_angle))
                y.append(radius * np.sin(v_angle) * np.sin(u_angle))
                z.append(radius * np.cos(v_angle) * z_compression)

    return np.array(x), np.array(y), np.array(z)


def plot_sphere(x, y, z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, marker='.', s=1)
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.show()


steps = 5  # Número de etapas da simulação
u_steps = 100  # Divisões longitudinais
v_steps = 50  # Divisões latitudinais

x, y, z = simulate_sphere_division(steps, u_steps, v_steps)
plot_sphere(x, y, z)
