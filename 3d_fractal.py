import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a new figure for the plot
fig = plt.figure()

# Create a 3D axes object for the plot
ax = fig.add_subplot(111, projection='3d')

# Define the transformation function that will be applied to the points in the fractal
def transform(points):
  new_points = []
  for point in points:
    x, y, z = point
    # Apply the transformation to the x, y, and z coordinates of the point
    new_x = x + y
    new_y = x + y
    new_z = x + y
    # Add the new point to the list of points
    new_points.append([new_x, new_y, new_z])
  # Return the list of transformed points
  return np.array(new_points)

# Define the recursive function to generate the points in the fractal
def draw_fractal(points, depth):
  if depth == 0:
    # Plot the points in the fractal on the 3D axes
    ax.scatter(points[:,0], points[:,1], points[:,2])
  else:
    # Generate the new points in the fractal by applying the transformation function
    new_points = transform(points)
    # Recursively call the function to generate the rest of the fractal
    draw_fractal(new_points, depth-1)

# Define the initial points in the fractal and the depth of the recursion
points = np.array([[0.0, 0.0, 0.0]])
depth = 5

# Call the recursive function to draw the fractal
draw_fractal(points, depth)

# Show the plot on the screen
plt.show()
