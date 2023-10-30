# Spencer: Can you program it such that the squares can be moves around my clicking and holding the left mouse button?

import pygame
import os

# Initialize Pygame
pygame.init()

# Create a window
screen = pygame.display.set_mode((800, 600))

# Define some colors (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Initialize font
font = pygame.font.SysFont(None, 36)

# Read the directory
directory_path = './files'  # Replace with your directory path
file_names = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

# Variable to hold file content
file_content = ""

# Variable to hold the square currently being dragged
dragging = None

# Position for each square
positions = {file_name: (50 + idx * 60, 50) for idx, file_name in enumerate(file_names)}

# Main event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            for file_name, (pos_x, pos_y) in positions.items():
                rect = pygame.Rect(pos_x, pos_y, 50, 50)
                if rect.collidepoint(x, y):
                    dragging = file_name
                    with open(os.path.join(directory_path, file_name), 'r') as f:
                        file_content = f.read()
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = None

    # Clear the screen
    screen.fill(WHITE)

    # Get mouse position
    x, y = pygame.mouse.get_pos()

    # Update positions if dragging
    if dragging:
        positions[dragging] = (x - 25, y - 25)

    # Render squares and file names based on hover
    for file_name, (pos_x, pos_y) in positions.items():
        rect = pygame.Rect(pos_x, pos_y, 50, 50)
        pygame.draw.rect(screen, BLUE, rect, 2)
        if rect.collidepoint(x, y):
            text = font.render(file_name, True, BLACK)
            text_rect = text.get_rect(center=(pos_x + 25, pos_y + 25))
            screen.blit(text, text_rect)

    # Render file content
    if file_content:
        y_offset = 150  # Starting Y-position for rendering file content
        for idx, line in enumerate(file_content.split('\n')):
            content_text = font.render(line, True, BLACK)
            screen.blit(content_text, [300, y_offset + idx * 40])

    # Update the display
    pygame.display.update()

# Clean up
pygame.quit()

# ChatGPT: 
# In this modified version, I added a dragging variable to keep track of which square is being dragged. 
# I also added a positions dictionary to keep track of the position of each square. 
# The positions are updated in the main loop if a square is being dragged.