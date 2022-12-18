import pygame
import math

# define the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# define the ball dimensions and position
BALL_RADIUS = 50
ball1_x = SCREEN_WIDTH // 3
ball1_y = SCREEN_HEIGHT // 3
ball2_x = SCREEN_WIDTH // 3 * 2
ball2_y = SCREEN_HEIGHT // 3
ball3_x = SCREEN_WIDTH // 2
ball3_y = SCREEN_HEIGHT // 3 * 2

# define the ball's velocity
ball1_vx = 3
ball1_vy = 0
ball2_vx = -3
ball2_vy = 3
ball3_vx = -3
ball3_vy = -3

# define the gravitational constant
GRAVITATIONAL_CONSTANT = 11

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

    # # calculate center of mass between other 2 balls

    # com_1_2_x = (ball1_x + ball2_x) // 2
    # com_1_3_x = (ball1_x + ball3_x) // 2
    # com_2_3_x = (ball2_x + ball3_x) // 2

    # com_1_2_y = (ball1_y + ball2_y) // 2
    # com_1_3_y = (ball1_y + ball3_y) // 2
    # com_2_3_y = (ball2_y + ball3_y) // 2

    # # calculate the distance between each ball and the center of mass of each of the other two balls
    # dx1_2_3 = com_2_3_x - ball1_x
    # dx2_3_1 = com_1_3_x - ball2_x
    # dx3_1_2 = com_1_2_x - ball3_x

    # dy1_2_3 = com_2_3_y - ball1_y
    # dy2_3_1 = com_1_3_y - ball2_y
    # dy3_1_2 = com_1_2_y - ball3_y

    # dist_1_2_3 = math.hypot(dx1_2_3, dy1_2_3)
    # dist_2_3_1 = math.hypot(dx2_3_1, dy2_3_1)
    # dist_3_1_2 = math.hypot(dx3_1_2, dy3_1_2)


    # # calculate the gravitational force
    # force_1_2_3 = GRAVITATIONAL_CONSTANT * ((BALL_RADIUS * BALL_RADIUS) / (dist_1_2_3 * dist_1_2_3))
    # force_2_3_1 = GRAVITATIONAL_CONSTANT * ((BALL_RADIUS * BALL_RADIUS) / (dist_2_3_1 * dist_2_3_1))
    # force_3_1_2 = GRAVITATIONAL_CONSTANT * ((BALL_RADIUS * BALL_RADIUS) / (dist_3_1_2 * dist_3_1_2))

    # # calculate the direction of the gravitational force
    # angle_1_2_3 = math.atan2(dy1_2_3, dx1_2_3)
    # angle_2_3_1 = math.atan2(dy2_3_1, dx2_3_1)
    # angle_3_1_2 = math.atan2(dy3_1_2, dx3_1_2)

    # # apply the gravitational force to the balls' velocities
    # ball1_vx += force_1_2_3 * math.cos(angle_1_2_3)
    # ball1_vy += force_1_2_3 * math.sin(angle_1_2_3)
    # ball2_vx += force_2_3_1 * math.cos(angle_2_3_1)
    # ball2_vy += force_2_3_1 * math.sin(angle_2_3_1)
    # ball2_vx += force_3_1_2 * math.cos(angle_3_1_2)
    # ball2_vy += force_3_1_2 * math.sin(angle_3_1_2)

    # calculate center of mass between other 2 balls

    # calculate the distance between all balls
    dx1_2 = ball2_x - ball1_x
    dx2_3 = ball3_x - ball2_x
    dx3_1 = ball1_x - ball3_x

    dy1_2 = ball2_y - ball1_y
    dy2_3 = ball3_y - ball2_y
    dy3_1 = ball1_y - ball3_y

    dist_1_2 = math.hypot(dx1_2, dy1_2)
    dist_2_3 = math.hypot(dx2_3, dy2_3)
    dist_3_1 = math.hypot(dx3_1, dy3_1)


    # calculate the gravitational force
    force_1_2 = GRAVITATIONAL_CONSTANT * ((BALL_RADIUS * BALL_RADIUS) / (dist_1_2 * dist_1_2))
    force_2_3 = GRAVITATIONAL_CONSTANT * ((BALL_RADIUS * BALL_RADIUS) / (dist_2_3 * dist_2_3))
    force_3_1 = GRAVITATIONAL_CONSTANT * ((BALL_RADIUS * BALL_RADIUS) / (dist_3_1 * dist_3_1))

    # calculate the direction of the gravitational force
    angle_1_2 = math.atan2(dy1_2, dx1_2)
    angle_2_3 = math.atan2(dy2_3, dx2_3)
    angle_3_1 = math.atan2(dy3_1, dx3_1)

    # apply the gravitational force to the balls' velocities
    ball1_vx += force_1_2 * math.cos(angle_1_2)
    ball1_vy += force_1_2 * math.sin(angle_1_2)
    ball1_vx -= force_3_1 * math.cos(angle_3_1)
    ball1_vy -= force_3_1 * math.sin(angle_3_1)

    ball2_vx += force_2_3 * math.cos(angle_2_3)
    ball2_vy += force_2_3 * math.sin(angle_2_3)
    ball2_vx -= force_1_2 * math.cos(angle_1_2)
    ball2_vy -= force_1_2 * math.sin(angle_1_2)

    ball3_vx += force_3_1 * math.cos(angle_3_1)
    ball3_vy += force_3_1 * math.sin(angle_3_1)
    ball3_vx += force_2_3 * math.cos(angle_2_3)
    ball3_vy += force_2_3 * math.sin(angle_2_3)

    # update the balls' positions
    ball1_x += ball1_vx
    ball1_y += ball1_vy
    ball2_x += ball2_vx
    ball2_y += ball2_vy
    ball3_x += ball3_vx
    ball3_y += ball3_vy

    # clear the screen
    screen.fill((0, 0, 0))

    # draw the balls
    pygame.draw.circle(screen, (255, 255, 255), (ball1_x, ball1_y), BALL_RADIUS)
    pygame.draw.circle(screen, (255, 255, 255), (ball2_x, ball2_y), BALL_RADIUS)

    # update the screen
    pygame.display.flip()

    # limit the frame rate
    clock.tick(60)