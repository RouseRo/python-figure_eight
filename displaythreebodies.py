import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV
df = pd.read_csv('three_body_simulation.csv')

# Plot trajectories
plt.figure(figsize=(10, 8))
for body in df['Body'].unique():
    body_data = df[df['Body'] == body]
    plt.plot(body_data['X'], body_data['Y'], label=f'Body {body}')

plt.title('Three Body Simulation Trajectory')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.legend()
plt.show()
