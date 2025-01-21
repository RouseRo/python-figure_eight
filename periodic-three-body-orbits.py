import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Gravitational constant
G = 1

# Masses of the three bodies
m1, m2, m3 = 1, 1, 1

# Initial positions and velocities
# (x, y, vx, vy) for each body
initial_state = [
    1, 0, 0, 0.5,  # Body 1
    -1, 0, 0, -0.5, # Body 2
    0, 1, -0.5, 0  # Body 3
]

def derivatives(t, state):
    x1, y1, vx1, vy1, x2, y2, vx2, vy2, x3, y3, vx3, vy3 = state
    
    r12 = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    r13 = np.sqrt((x3 - x1)**2 + (y3 - y1)**2)
    r23 = np.sqrt((x3 - x2)**2 + (y3 - y2)**2)
    
    ax1 = G * m2 * (x2 - x1) / r12**3 + G * m3 * (x3 - x1) / r13**3
    ay1 = G * m2 * (y2 - y1) / r12**3 + G * m3 * (y3 - y1) / r13**3
    
    ax2 = G * m1 * (x1 - x2) / r12**3 + G * m3 * (x3 - x2) / r23**3
    ay2 = G * m1 * (y1 - y2) / r12**3 + G * m3 * (y3 - y2) / r23**3
    
    ax3 = G * m1 * (x1 - x3) / r13**3 + G * m2 * (x2 - x3) / r23**3
    ay3 = G * m1 * (y1 - y3) / r13**3 + G * m2 * (y2 - y3) / r23**3
    
    return [vx1, vy1, ax1, ay1, vx2, vy2, ax2, ay2, vx3, vy3, ax3, ay3]

# Time span for the simulation
t_span = (0, 10)

# Solve the differential equations
solution = solve_ivp(derivatives, t_span, initial_state, t_eval=np.linspace(0, 10, 1000))

# Extract the positions for plotting
x1, y1 = solution.y[0], solution.y[1]
x2, y2 = solution.y[4], solution.y[5]
x3, y3 = solution.y[8], solution.y[9]

# Plot the orbits
plt.figure(figsize=(10, 8))
plt.plot(x1, y1, label='Body 1')
plt.plot(x2, y2, label='Body 2')
plt.plot(x3, y3, label='Body 3')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Periodic Planar Three-Body Orbits')
plt.grid()
plt.show()