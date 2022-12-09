import matplotlib.pyplot as plt
from random import randint

# Set the size of the coastline
width = 100
height = 100

# Initialize the coastline matrix with all zeros
coastline = [[0 for x in range(width)] for y in range(height)]

# Set the starting point for the coastline
x = randint(0, width-1)
y = randint(0, height-1)
coastline[y][x] = 1

# Set the number of iterations for the fractal algorithm
n = 10000

# Apply the fractal algorithm to generate the coastline
for i in range(n):
    # Choose a random direction (up, down, left, or right)
    direction = randint(0, 3)
    if direction == 0:
        y = y - 1
    elif direction == 1:
        y = y + 1
    elif direction == 2:
        x = x - 1
    elif direction == 3:
        x = x + 1

    # Make sure the coordinates are valid (i.e. within the bounds of the matrix)
    x = max(0, min(x, width-1))
    y = max(0, min(y, height-1))

    # Set the value of the matrix at the new coordinates to 1
    coastline[y][x] = 1

# Use matplotlib to visualize the coastline
plt.imshow(coastline, cmap='binary')
plt.show()