import pygame
import os

# Initialize Pygame
pygame.init()

# Create a window
screen = pygame.display.set_mode((800, 600))

# Define some colors (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
font = pygame.font.SysFont(None, 36)

# Read the directory
directory_path = './files'  # Replace with your directory path
file_names = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

# Main event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Render file names
    for idx, file_name in enumerate(file_names):
        text = font.render(file_name, True, BLACK)
        screen.blit(text, [50, 50 + idx * 40])

    # Update the display
    pygame.display.update()

# Clean up
pygame.quit()
