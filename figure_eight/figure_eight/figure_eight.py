# figure_eight/figure_eight.py

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Gravitational constant (set to 1 for simplicity)
G = 1.0

# Masses of the three bodies (all equal)
m1 = m2 = m3 = 1.0

def equations_of_motion(t, state):
    """
    Computes the derivatives of the state vector.
    """
    # Unpack the state vector
    x1, y1, x2, y2, x3, y3, vx1, vy1, vx2, vy2, vx3, vy3 = state

    # Positions
    r1 = np.array([x1, y1])
    r2 = np.array([x2, y2])
    r3 = np.array([x3, y3])

    # Compute pairwise distance vectors
    r12 = r2 - r1
    r13 = r3 - r1
    r23 = r3 - r2

    # Compute magnitudes of distance vectors
    r12_norm = np.linalg.norm(r12)
    r13_norm = np.linalg.norm(r13)
    r23_norm = np.linalg.norm(r23)

    # Compute accelerations
    a1 = G * m2 * r12 / r12_norm**3 + G * m3 * r13 / r13_norm**3
    a2 = G * m1 * -r12 / r12_norm**3 + G * m3 * r23 / r23_norm**3
    a3 = G * m1 * -r13 / r13_norm**3 + G * m2 * -r23 / r23_norm**3

    # Flatten the derivatives
    derivatives = np.array([
        vx1, vy1,
        vx2, vy2,
        vx3, vy3,
        a1[0], a1[1],
        a2[0], a2[1],
        a3[0], a3[1]
    ])

    return derivatives

def main():
    # Initial positions and velocities for the figure-eight solution
    # Positions
    x1_0 = 0.97000436
    y1_0 = -0.24308753
    x2_0 = -x1_0
    y2_0 = -y1_0
    x3_0 = 0.0
    y3_0 = 0.0

    # Velocities
    vx1_0 = 0.4662036850
    vy1_0 = 0.4323657300
    vx2_0 = vx1_0
    vy2_0 = vy1_0
    vx3_0 = -2 * vx1_0
    vy3_0 = -2 * vy1_0

    # Initial state vector
    initial_state = np.array([
        x1_0, y1_0,
        x2_0, y2_0,
        x3_0, y3_0,
        vx1_0, vy1_0,
        vx2_0, vy2_0,
        vx3_0, vy3_0
    ])

    # Time span for the simulation
    t_span = (0, 6.3259)  # Period of the figure-eight orbit
    t_eval = np.linspace(t_span[0], t_span[1], 1000)

    # Integrate the equations of motion
    solution = solve_ivp(
        equations_of_motion,
        t_span,
        initial_state,
        t_eval=t_eval,
        rtol=1e-10,
        atol=1e-10
    )

    # Extract positions
    x1 = solution.y[0]
    y1 = solution.y[1]
    x2 = solution.y[2]
    y2 = solution.y[3]
    x3 = solution.y[4]
    y3 = solution.y[5]

    # Plotting the trajectories
    plt.figure(figsize=(8, 8))
    plt.plot(x1, y1, '-', label='Body 1')
    plt.plot(x2, y2, '-', label='Body 2')
    plt.plot(x3, y3, '-', label='Body 3')

    # Plot starting points
    plt.plot(x1[0], y1[0], 'o', color='tab:blue')
    plt.plot(x2[0], y2[0], 'o', color='tab:orange')
    plt.plot(x3[0], y3[0], 'o', color='tab:green')

    plt.legend()
    plt.title('Figure-Eight Solution of the Three-Body Problem')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.axis('equal')
    plt.show()

if __name__ == '__main__':
    main()