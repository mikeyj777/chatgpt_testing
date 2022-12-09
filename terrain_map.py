import numpy as np
import matplotlib.pyplot as plt

# Set the size of the terrain map
width = 256
height = 256

# Generate a height map using Perlin noise
noise = np.random.randn(width, height)

# Create a color map to use for the terrain
color_map = plt.cm.terrain

# Plot the height map on the screen
plt.imshow(noise, cmap=color_map)

# Show the plot on the screen
plt.show()