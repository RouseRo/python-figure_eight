# figure_eight_animated/figure_eight_animated.py
# Author: Robert K. Rouse with help from OpenAI "o1"

import numpy as np
from scipy.integrate import solve_ivp
import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Figure-Eight Three-Body Animation")

# Colors
BLACK = (0, 0, 0)
BODY_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Red, Green, Blue

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
    total_time = 6.3259  # Period of the figure-eight orbit
    # t_eval = np.linspace(0, total_time, 10000)
    t_eval = np.linspace(0, total_time, 500)

    # Integrate the equations of motion
    solution = solve_ivp(
        equations_of_motion,
        (0, total_time),
        initial_state,
        t_eval=t_eval,
        rtol=1e-10,
        atol=1e-10
    )

    # Extract positions
    positions = solution.y[:6]

    # Scale positions for display
    max_coord = np.max(np.abs(positions))
    scale = (WIDTH // 2 - 50) / max_coord  # Leave some margin

    # Center of the screen
    center_x = WIDTH // 2
    center_y = HEIGHT // 2

    # Time settings
    clock = pygame.time.Clock()
    sim_speed = 1.0  # Simulation speed multiplier

    # Animation loop variables
    running = True
    index = 0
    time_step = t_eval[1] - t_eval[0]

    while running:
        clock.tick(60)  # Limit to 60 FPS

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Optional: Add interactivity with keyboard
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                # Speed up simulation
                elif event.key == pygame.K_UP:
                    sim_speed *= 1.1
                # Slow down simulation
                elif event.key == pygame.K_DOWN:
                    sim_speed /= 1.1

        # Clear the screen
        SCREEN.fill(BLACK)

        # Update index based on simulation speed
        index += int(sim_speed)
        if index >= len(t_eval):
            index = 0  # Loop the animation

        # Get current positions
        x1 = positions[0, index]
        y1 = positions[1, index]
        x2 = positions[2, index]
        y2 = positions[3, index]
        x3 = positions[4, index]
        y3 = positions[5, index]

        # Convert to screen coordinates
        def to_screen(x, y):
            return int(center_x + x * scale), int(center_y - y * scale)

        pos1 = to_screen(x1, y1)
        pos2 = to_screen(x2, y2)
        pos3 = to_screen(x3, y3)

        # Draw bodies
        pygame.draw.circle(SCREEN, BODY_COLORS[0], pos1, 8)
        pygame.draw.circle(SCREEN, BODY_COLORS[1], pos2, 8)
        pygame.draw.circle(SCREEN, BODY_COLORS[2], pos3, 8)

        # Optional: Draw trails (simple implementation)
        trail_length = 75  # Adjust for longer trails
        for i in range(trail_length):
            idx = index - i * int(sim_speed)
            if idx < 0:
                break
            alpha = max(255 - i * (255 // trail_length), 0)
            color1 = (*BODY_COLORS[0], alpha)
            color2 = (*BODY_COLORS[1], alpha)
            color3 = (*BODY_COLORS[2], alpha)

            x1_trail = positions[0, idx]
            y1_trail = positions[1, idx]
            x2_trail = positions[2, idx]
            y2_trail = positions[3, idx]
            x3_trail = positions[4, idx]
            y3_trail = positions[5, idx]

            pos1_trail = to_screen(x1_trail, y1_trail)
            pos2_trail = to_screen(x2_trail, y2_trail)
            pos3_trail = to_screen(x3_trail, y3_trail)

            # Draw trail circles with decreasing alpha
            trail_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            pygame.draw.circle(trail_surface, color1, pos1_trail, 4)
            pygame.draw.circle(trail_surface, color2, pos2_trail, 4)
            pygame.draw.circle(trail_surface, color3, pos3_trail, 4)
            SCREEN.blit(trail_surface, (0, 0))

        # Update the display
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()