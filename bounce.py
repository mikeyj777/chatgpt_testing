import pygame

# define the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# define the ball dimensions and position
BALL_RADIUS = 50
ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2

# define the ball's velocity
ball_vx = 5
ball_vy = 5

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

    # update the ball position
    ball_x += ball_vx
    ball_y += ball_vy

    # check if the ball has collided with a wall
    if ball_x + BALL_RADIUS > SCREEN_WIDTH or ball_x - BALL_RADIUS < 0:
        ball_vx *= -1
    if ball_y + BALL_RADIUS > SCREEN_HEIGHT or ball_y - BALL_RADIUS < 0:
        ball_vy *= -1

    # clear the screen
    screen.fill((0, 0, 0))

    # draw the ball
    pygame.draw.circle(screen, (255, 255, 255), (ball_x, ball_y), BALL_RADIUS)

    # update the screen
    pygame.display.flip()

    # limit the frame rate
    clock.tick(60)