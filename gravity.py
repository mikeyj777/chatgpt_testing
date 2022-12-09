import pygame
import math

# define the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# define the ball dimensions and position
LARGE_BALL_RADIUS = 100
SMALL_BALL_RADIUS = 50
large_ball_x = SCREEN_WIDTH // 2
large_ball_y = SCREEN_HEIGHT // 2
small_ball_x = large_ball_x + 200
small_ball_y = large_ball_y

# define the ball's velocity
small_ball_vx = 0
small_ball_vy = 10

# define the gravitational constant
GRAVITATIONAL_CONSTANT = 3

# initialize Pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# create a clock to control the frame rate
clock = pygame.time.Clock()

# main game loop
while True:
    # process events
    for event in pygame.event.get():
        # check if the user closed the window
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # calculate the distance between the two balls
    dx = large_ball_x - small_ball_x
    dy = large_ball_y - small_ball_y
    distance = math.hypot(dx, dy)

    # calculate the gravitational force
    force = GRAVITATIONAL_CONSTANT * ((LARGE_BALL_RADIUS * SMALL_BALL_RADIUS) / (distance * distance))

    # calculate the direction of the gravitational force
    angle = math.atan2(dy, dx)

    # apply the gravitational force to the small ball's velocity
    small_ball_vx += force * math.cos(angle)
    small_ball_vy += force * math.sin(angle)

    # update the small ball's position
    small_ball_x += small_ball_vx
    small_ball_y += small_ball_vy

    # clear the screen
    screen.fill((0, 0, 0))

    # draw the balls
    pygame.draw.circle(screen, (255, 255, 255), (large_ball_x, large_ball_y), LARGE_BALL_RADIUS)
    pygame.draw.circle(screen, (255, 255, 255), (small_ball_x, small_ball_y), SMALL_BALL_RADIUS)

    # update the screen
    pygame.display.flip()

    # limit the frame rate
    clock.tick(60)