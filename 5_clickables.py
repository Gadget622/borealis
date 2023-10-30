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

# Main event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            for idx, file_name in enumerate(file_names):
                if 50 <= x <= 250 and 50 + idx * 40 <= y <= 90 + idx * 40:
                    print(f"Clicked on {file_name}")

    # Clear the screen
    screen.fill(WHITE)

    # Render file names and rectangles
    for idx, file_name in enumerate(file_names):
        text = font.render(file_name, True, BLACK)
        text_rect = text.get_rect(topleft=(60, 60 + idx * 40))
        screen.blit(text, text_rect)
        
        rect = pygame.Rect(50, 50 + idx * 40, 200, 40)
        pygame.draw.rect(screen, BLUE, rect, 2)

    # Update the display
    pygame.display.update()

# Clean up
pygame.quit()
