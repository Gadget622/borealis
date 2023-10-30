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

# Main event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            for idx, file_name in enumerate(file_names):
                rect = pygame.Rect(50 + idx * 60, 50, 50, 50)
                if rect.collidepoint(x, y):
                    with open(os.path.join(directory_path, file_name), 'r') as f:
                        file_content = f.read()

    # Clear the screen
    screen.fill(WHITE)

    # Get mouse position
    x, y = pygame.mouse.get_pos()

    # Render squares and file names based on hover
    for idx, file_name in enumerate(file_names):
        rect = pygame.Rect(50 + idx * 60, 50, 50, 50)
        pygame.draw.rect(screen, BLUE, rect, 2)
        if rect.collidepoint(x, y):
            text = font.render(file_name, True, BLACK)
            text_rect = text.get_rect(center=(50 + idx * 60 + 25, 50 + 25))
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
