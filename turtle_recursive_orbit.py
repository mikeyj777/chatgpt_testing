import turtle
import math

# Set the turtle speed and colors
turtle.speed(0)
colors = ["red", "green", "blue", "purple", "orange"]

# Define a Ball class to represent the balls
class Ball:
  def __init__(self, x, y, radius, parent=None):
    self.x = x
    self.y = y
    self.radius = radius
    self.parent = parent

  # Draw the ball on the screen
  def draw(self):
    turtle.penup()
    turtle.goto(self.x, self.y)
    turtle.pendown()
    turtle.color(colors[self.radius % len(colors)])
    turtle.dot(self.radius)

  # Update the position of the ball
  def update(self):
    # If the ball has a parent, move it in an orbit around the parent
    if self.parent:
      # Calculate the new angle based on the parent's position
      angle = math.atan2(self.parent.y - self.y, self.parent.x - self.x)
      self.x = self.parent.x - self.parent.radius * math.cos(angle)
      self.y = self.parent.y - self.parent.radius * math.sin(angle)

    # If the ball is the root, move it in a circle
    else:
      self.x = self.x + self.radius * math.cos(turtle.heading() / 180 * math.pi)
      self.y = self.y + self.radius * math.sin(turtle.heading() / 180 * math.pi)
      turtle.setheading(turtle.heading() + 1)

  # Recursively add smaller balls that orbit this ball
  def add_child(self):
    # Create a new ball with the parent set to this ball
    child = Ball(self.x, self.y, self.radius / 2, self)

    # Add the child to the list of balls
    balls.append(child)

    # Recursively add more children to the child
    child.add_child()

# Initialize the list of balls
balls = []

# Create the root ball and add it to the list
root = Ball(0, 0, 100)
balls.append(root)

# Main loop
while True:
  # Clear the screen
  turtle.clear()

  # Update and draw each ball
  for ball in balls:
    ball.update()
    ball.draw()

  # Randomly add more balls to the root ball
  if turtle.getcanvas().after(1, None) == "b1-Motion":
    root.add_child()
