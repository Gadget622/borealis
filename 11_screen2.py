# Spencer: Can you alter the code such that the contents of the file are rendered in a second window instead of being opened?

# ChatGPT: Sure! I've added a new Pygame surface named "second_screen" to render the contents of the file.
# When you right-click a square, this second window will update to display the content of the selected file.

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

# Variable to hold file content for second screen
second_screen_content = ""

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
                    if event.button == 1:  # Left click
                        dragging = file_name
                        with open(os.path.join(directory_path, file_name), 'r') as f:
                            file_content = f.read()
                    elif event.button == 3:  # Right click
                        with open(os.path.join(directory_path, file_name), 'r') as f:
                            # Create a second window for rendering file content
                            second_screen = pygame.display.set_mode((400, 300))
                            # Clear the second screen
                            second_screen.fill(WHITE)
                            second_screen_content = f.read()
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = None

    # Clear the main screen
    screen.fill(WHITE)


    # Get mouse position
    x, y = pygame.mouse.get_pos()

    # Update positions if dragging
    if dragging:
        positions[dragging] = (x - 25, y - 25)

    # Render squares and file names on main screen
    for file_name, (pos_x, pos_y) in positions.items():
        rect = pygame.Rect(pos_x, pos_y, 50, 50)
        pygame.draw.rect(screen, BLUE, rect, 2)
        if rect.collidepoint(x, y):
            text = font.render(file_name, True, BLACK)
            text_rect = text.get_rect(center=(pos_x + 25, pos_y + 25))
            screen.blit(text, text_rect)

    # Render file content on the second screen
    if second_screen_content:
        y_offset = 10  # Starting Y-position for rendering file content
        for idx, line in enumerate(second_screen_content.split('\n')):
            content_text = font.render(line, True, BLACK)
            second_screen.blit(content_text, [10, y_offset + idx * 40])

    # Update the displays
    pygame.display.update()

# Clean up
pygame.quit()
