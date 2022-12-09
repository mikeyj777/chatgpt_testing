import pygame

# Set the size of the window
width = 800
height = 600

# Initialize pygame
pygame.init()

# Create the window
window = pygame.display.set_mode((width, height))

# Set the title of the window
pygame.display.set_caption("Character Battle")

# Load the images for the characters
character1_image = pygame.image.load("assets/character_1.jpg")
character2_image = pygame.image.load("assets/character_2.jpg")

# Set the initial positions of the characters
character1_x = 100
character1_y = 100
character2_x = 600
character2_y = 100

# Set the initial health of the characters
character1_health = 100
character2_health = 100

# Set the speed of the characters
character_speed = 5

# Set the font for displaying text
font = pygame.font.Font("freesansbold.ttf", 32)

# Set the colors for the characters and the text
white = (255, 255, 255)
red = (255, 0, 0)

# Main game loop
while True:
    # Check for events (e.g. key presses, mouse clicks)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Move the characters
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        character1_y -= character_speed
    if keys[pygame.K_s]:
        character1_y += character_speed
    if keys[pygame.K_a]:
        character1_x -= character_speed
    if keys[pygame.K_d]:
        character1_x += character_speed
    if keys[pygame.K_UP]:
        character2_y -= character_speed
    if keys[pygame.K_DOWN]:
        character2_y += character_speed
    if keys[pygame.K_LEFT]:
        character2_x -= character_speed
    if keys[pygame.K_RIGHT]:
        character2_x += character_speed

    # Check for collisions and reduce the health of the characters if necessary
    if character1_x < character2_x + character2_image.get_width() and \
       character1_x + character1_image.get_width() > character2_x and \
       character1_y < character2_y + character2_image.get_height() and \
       character1_y + character1_image.get_height() > character2_y:
        character1_health -= 10
        character2_health -= 10

    # Clear the window
    window.fill((0, 0, 0))

    # Draw the characters
    window.blit(character1_image, (character1_x, character1_y))
    window.blit(character2_image, (character2_x, character2_y))