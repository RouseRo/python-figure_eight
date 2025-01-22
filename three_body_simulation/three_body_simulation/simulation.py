# three_body_simulation/simulation.py

import numpy as np
from scipy.integrate import solve_ivp
import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Three-Body Simulation")

# Colors
BLACK = (0, 0, 0)
BODY_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Red, Green, Blue

# Font for displaying text
FONT = pygame.font.SysFont(None, 18)

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

def get_figure_eight_initial_conditions():
    """
    Returns the initial conditions for the Figure-Eight Solution.
    """
    # Positions
    x1 = 0.97000436
    y1 = -0.24308753
    x2 = -x1
    y2 = -y1
    x3 = 0.0
    y3 = 0.0

    # Velocities
    vx1 = 0.4662036850
    vy1 = 0.4323657300
    vx2 = vx1
    vy2 = vy1
    vx3 = -2 * vx1
    vy3 = -2 * vy1

    initial_state = np.array([
        x1, y1, x2, y2, x3, y3,
        vx1, vy1, vx2, vy2, vx3, vy3
    ])

    total_time = 6.3259  # Period of the figure-eight orbit

    return initial_state, total_time

def get_lagrange_initial_conditions():
    """
    Returns the initial conditions for Lagrange's Equilateral Triangle Solution.
    """
    # Equilateral triangle positions
    angle = np.radians(0)
    r = 0.2  # Distance from center
    x1 = r * np.cos(angle)
    y1 = r * np.sin(angle)
    x2 = r * np.cos(angle + 2 * np.pi / 3)
    y2 = r * np.sin(angle + 2 * np.pi / 3)
    x3 = r * np.cos(angle + 4 * np.pi / 3)
    y3 = r * np.sin(angle + 4 * np.pi / 3)

    # Velocities for circular motion
    omega = np.sqrt(G * (m1 + m2 + m3) / r**3)
    vx1 = -omega * y1
    vy1 = omega * x1
    vx2 = -omega * y2
    vy2 = omega * x2
    vx3 = -omega * y3
    vy3 = omega * x3

    initial_state = np.array([
        x1, y1, x2, y2, x3, y3,
        vx1, vy1, vx2, vy2, vx3, vy3
    ])

    total_time = 2 * np.pi / omega  # Period of the circular orbit // was 2 *

    return initial_state, total_time
def get_euler_colinear_initial_conditions():
    """
    Returns the initial conditions for Euler's Colinear Solution.
    """
    # Positions along x-axis
    x1 = -1.0
    y1 = 0.0
    x2 = 0.0
    y2 = 0.0
    x3 = 1.0
    y3 = 0.0

    # Velocities
    vx1 = 0.0
    vy1 = 0.5
    vx2 = 0.0
    vy2 = 0.0
    vx3 = 0.0
    vy3 = -0.5

    initial_state = np.array([
        x1, y1, x2, y2, x3, y3,
        vx1, vy1, vx2, vy2, vx3, vy3
    ])

    total_time = 10.0  # Adjust as necessary for full orbit

    return initial_state, total_time


def get_broucke_henon_initial_conditions():
    """
    Returns the initial conditions for a Broucke-Hénon Retrograde Orbit.
    """
    # Approximate initial conditions from numerical simulations
    x1 = 0.0
    y1 = 0.0
    x2 = 1.0
    y2 = 0.0
    x3 = -1.0
    y3 = 0.0

    vx1 = 0.347111
    vy1 = 0.532728
    vx2 = -0.694222
    vy2 = 0.0
    vx3 = 0.347111
    vy3 = -0.532728

    initial_state = np.array([
        x1, y1, x2, y2, x3, y3,
        vx1, vy1, vx2, vy2, vx3, vy3
    ])

    total_time = 20.0  # Adjust as necessary

    return initial_state, total_time


def get_butterfly_initial_conditions():
    """
    Returns the initial conditions for the Butterfly Orbit.
    """
    # Approximate initial conditions from simulations
    x1 = 0.0
    y1 = 0.0
    x2 = 1.0
    y2 = 0.0
    x3 = -1.0
    y3 = 0.0

    vx1 = 0.0
    vy1 = 0.3
    vx2 = -0.25
    vy2 = -0.15
    vx3 = 0.25
    vy3 = -0.15

    initial_state = np.array([
        x1, y1, x2, y2, x3, y3,
        vx1, vy1, vx2, vy2, vx3, vy3
    ])

    total_time = 20.0

    return initial_state, total_time


def get_yin_yang_initial_conditions():
    """
    Returns the initial conditions for the Yin-Yang Orbit.
    """
    # Approximate initial conditions
    x1 = 0.0
    y1 = 1.0
    x2 = 0.0
    y2 = -1.0
    x3 = 0.0
    y3 = 0.0

    vx1 = 0.6
    vy1 = 0.0
    vx2 = -0.6
    vy2 = 0.0
    vx3 = 0.0
    vy3 = 0.0

    initial_state = np.array([
        x1, y1, x2, y2, x3, y3,
        vx1, vy1, vx2, vy2, vx3, vy3
    ])

    total_time = 20.0

    return initial_state, total_time


def get_dragonfly_initial_conditions():
    """
    Returns the initial conditions for the Dragonfly Orbit.
    """
    # Approximate initial conditions
    x1 = -0.5
    y1 = 0.0
    x2 = 0.5
    y2 = 0.0
    x3 = 0.0
    y3 = 0.0

    vx1 = 0.0
    vy1 = 0.5
    vx2 = 0.0
    vy2 = -0.5
    vx3 = 0.0
    vy3 = 0.0

    initial_state = np.array([
        x1, y1, x2, y2, x3, y3,
        vx1, vy1, vx2, vy2, vx3, vy3
    ])

    total_time = 20.0

    return initial_state, total_time


def get_mobius_initial_conditions():
    """
    Returns the initial conditions for the Möbius Solution.
    """
    # Approximate initial conditions
    x1 = 1.0
    y1 = 0.0
    x2 = -0.5
    y2 = np.sqrt(3)/2
    x3 = -0.5
    y3 = -np.sqrt(3)/2

    # Velocities
    vx1 = 0.0
    vy1 = -0.5
    vx2 = 0.433
    vy2 = 0.25
    vx3 = -0.433
    vy3 = 0.25

    initial_state = np.array([
        x1, y1, x2, y2, x3, y3,
        vx1, vy1, vx2, vy2, vx3, vy3
    ])

    total_time = 20.0

    return initial_state, total_time

def main():
    # Default to Figure-Eight Solution
    initial_state, total_time = get_figure_eight_initial_conditions()
    solution_name = 'Figure-Eight Solution'

    # Time settings
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
        reload_solution = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Handle keyboard input
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                # Speed up simulation
                elif event.key == pygame.K_UP:
                    sim_speed *= 1.1
                # Slow down simulation
                elif event.key == pygame.K_DOWN:
                    sim_speed /= 1.1
                # Select Figure-Eight Solution
                elif event.key == pygame.K_f:
                    initial_state, total_time = get_figure_eight_initial_conditions()
                    solution_name = 'Figure-Eight Solution'
                    reload_solution = True
                # Select Lagrange's Solution
                elif event.key == pygame.K_l:
                    initial_state, total_time = get_lagrange_initial_conditions()
                    solution_name = "Lagrange's Solution"
                    reload_solution = True
                # Select Euler's Colinear Solution
                elif event.key == pygame.K_e:
                    initial_state, total_time = get_euler_colinear_initial_conditions()
                    solution_name = "Euler's Colinear Solution"
                    reload_solution = True
                # Select Broucke-Hénon Retrograde Orbit
                elif event.key == pygame.K_b:
                    initial_state, total_time = get_broucke_henon_initial_conditions()
                    solution_name = "Broucke-Hénon Retrograde Orbit"
                    reload_solution = True
                # Select Butterfly Orbit
                elif event.key == pygame.K_y:  # Using 'Y' for Butterfly
                    initial_state, total_time = get_butterfly_initial_conditions()
                    solution_name = "Butterfly Orbit"
                    reload_solution = True
                # Select Yin-Yang Orbit
                elif event.key == pygame.K_u:  # Using 'U' for Yin-Yang
                    initial_state, total_time = get_yin_yang_initial_conditions()
                    solution_name = "Yin-Yang Orbit"
                    reload_solution = True
                # Select Dragonfly Orbit
                elif event.key == pygame.K_d:
                    initial_state, total_time = get_dragonfly_initial_conditions()
                    solution_name = "Dragonfly Orbit"
                    reload_solution = True
                # Select Möbius Solution
                elif event.key == pygame.K_m:
                    initial_state, total_time = get_mobius_initial_conditions()
                    solution_name = "Möbius Solution"
                    reload_solution = True

            # Outside the event loop:

            if reload_solution:
                t_eval = np.linspace(0, total_time, 10000)
                solution = solve_ivp(
                    equations_of_motion,
                    (0, total_time),
                    initial_state,
                    t_eval=t_eval,
                    rtol=1e-10,
                    atol=1e-10
                )
                
                positions = solution.y[:6]
                max_coord = np.max(np.abs(positions))
                scale = (WIDTH // 2 - 50) / max_coord
                index = 0  # Reset index

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

        # Optional: Draw trails
        trail_length = 100
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

        # Display solution name
        text_surface = FONT.render(f"Current Solution: {solution_name}", True, (255, 255, 255))
        SCREEN.blit(text_surface, (20, 20))

        # Display instructions
        instructions = [
            "Press 'F' for Figure-Eight Solution",
            "Press 'L' for Lagrange's Solution",
            "Press 'E' for Euler's Colinear Solution",
            "Press 'B' for Broucke-Hénon Orbit",
            "Press 'Y' for Butterfly Orbit",
            "Press 'U' for Yin-Yang Orbit",
            "Press 'D' for Dragonfly Orbit",
            "Press 'M' for Möbius Solution",
            "Press UP/DOWN to Speed Up/Slow Down",
            "Press ESC to Quit"
        ]
        for i, instruction in enumerate(instructions):
            instr_surface = FONT.render(instruction, True, (200, 200, 200))
            SCREEN.blit(instr_surface, (20, 40 + i * 20))

        # Update the display
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()