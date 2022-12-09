from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Initialize the OpenGL environment
glutInit()

# Create a window for the 3D environment
glutCreateWindow("3D Environment")

# Set the background color to blue
glClearColor(0.0, 0.0, 1.0, 1.0)

# Define a function that will be called on each frame to update the 3D environment
def update():
  # Clear the color and depth buffers
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

  # Specify the modelview matrix
  glMatrixMode(GL_MODELVIEW)

  # Reset the modelview matrix to the identity matrix
  glLoadIdentity()

  # Apply a translation transformation to move the camera
  glTranslatef(0.0, 0.0, -5.0)

  # Apply a rotation transformation to rotate the objects
  glRotatef(45.0, 1.0, 1.0, 0.0)

  # Define the vertices and faces of a cube
  glBegin(GL_QUADS)
  glVertex3f(-1.0, -1.0, -1.0)
  glVertex3f(-1.0, 1.0, -1.0)
  glVertex3f(1.0, 1.0, -1.0)
  glVertex3f(1.0, -1.0, -1.0)