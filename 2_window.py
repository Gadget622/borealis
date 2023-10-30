import pygame

# Initialize Pygame
pygame.init()

# Create a window
screen = pygame.display.set_mode((800, 600))

# Set up the colors (RGB)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Main event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw a red rectangle: (surface, color, [x, y, width, height])
    pygame.draw.rect(screen, RED, [50, 50, 100, 100])

    # Draw a green circle: (surface, color, (x, y), radius)
    pygame.draw.circle(screen, GREEN, (400, 300), 50)

    # Update the display
    pygame.display.update()

# Clean up
pygame.quit()
