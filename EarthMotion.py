import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
RADIUS = 1.0  # Orbital radius (AU)
PERIOD = 365.25  # Orbital period (days)
NUM_FRAMES = 100  # Number of frames in the animation

# Calculate the angular velocity
omega = 2 * np.pi / PERIOD

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.set_title('Circular Motion of Earth around the Sun')

# Plot the Sun
sun = plt.Circle((0, 0), 0.1, color='yellow')
ax.add_artist(sun)

# Plot the Earth's orbit
orbit = plt.Circle((0, 0), RADIUS, color='blue', fill=False)
ax.add_artist(orbit)

# Initialize the Earth point
earth, = ax.plot([], [], 'o', color='green')

# Function to update the frame
def update(frame):
    # Calculate the new position of Earth
    theta = omega * frame * (PERIOD / NUM_FRAMES)
    x = RADIUS * np.cos(theta)
    y = RADIUS * np.sin(theta)
    earth.set_data([x], [y])
    return earth,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=NUM_FRAMES, interval=50, blit=True)

# Show the animation
plt.show()
