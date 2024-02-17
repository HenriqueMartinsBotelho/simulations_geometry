import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def simulate_conical_spiral(steps, n_turns, points_per_turn):
    # Parâmetros para controlar o tamanho e a forma da espiral
    max_radius = 1.0
    height = 2.0

    x, y, z = [], [], []

    for step in range(steps + 1):
        for point in range(points_per_turn * n_turns):
            # Aumenta o raio e a altura com o passar dos passos
            radius = (point / (points_per_turn * n_turns)) * \
                max_radius * (1 + 0.5 * step / steps)
            angle = 2 * np.pi * point / points_per_turn
            z_pos = (height * point / (points_per_turn * n_turns)) * \
                (1 + 0.5 * step / steps)

            x.append(radius * np.cos(angle))
            y.append(radius * np.sin(angle))
            z.append(z_pos)

    return np.array(x), np.array(y), np.array(z)


def plot_conical_spiral(x, y, z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z, marker='.', linestyle='none', markersize=2)
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.show()


steps = 5  # Número de etapas da simulação
n_turns = 10  # Número de voltas completas na espiral
points_per_turn = 100  # Pontos por volta para definir a espiral

x, y, z = simulate_conical_spiral(steps, n_turns, points_per_turn)
plot_conical_spiral(x, y, z)
