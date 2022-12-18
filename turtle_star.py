import turtle

# Set the turtle speed and color
turtle.speed(0)
turtle.color("orange")

def draw_star(x, y, size):
  # Stop the recursion when the size is small enough
  if size < 10:
    return

  # Save the turtle's current state
  turtle.penup()
  turtle.goto(x, y)
  turtle.pendown()

  # Draw the star
  for i in range(5):
    turtle.forward(size)
    turtle.right(144)

  # Recursively draw smaller stars
  draw_star(x + size, y, size / 2)
  draw_star(x - size, y, size / 2)
  draw_star(x, y + size, size / 2)
  draw_star(x, y - size, size / 2)

# Draw the initial star
draw_star(0, 0, 100)
