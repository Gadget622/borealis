# Spencer: Open a virtual window that I can click and drag much like the squares themselves.
# Make them have clickable x's like at the top-right of any regular window that closes the virtual windows.

# ChatGPT: Added virtual window support. Each virtual window appears when a square is clicked. 
# You can drag these windows and close them using a clickable 'X' at the top-right corner.

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
RED = (255, 0, 0)

# Initialize font
font = pygame.font.SysFont(None, 36)

# Read the directory
directory_path = './files'
file_names = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

# Variable to hold file content
file_content = ""

# Variable to hold the square or window currently being dragged
dragging = None

# Position for each square
positions = {file_name: (50 + idx * 60, 50) for idx, file_name in enumerate(file_names)}

# Virtual windows
virtual_windows = {}

# Main event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            clicked = False
            for file_name, (pos_x, pos_y) in positions.items():
                rect = pygame.Rect(pos_x, pos_y, 50, 50)
                if rect.collidepoint(x, y):
                    dragging = ('square', file_name)
                    virtual_windows[file_name] = (300, 300)
                    clicked = True
                    break
            if not clicked:
                for file_name, (win_x, win_y) in virtual_windows.items():
                    win_rect = pygame.Rect(win_x, win_y, 200, 200)
                    close_rect = pygame.Rect(win_x + 180, win_y + 10, 10, 10)
                    if win_rect.collidepoint(x, y):
                        dragging = ('window', file_name)
                        clicked = True
                        break
                    elif close_rect.collidepoint(x, y):
                        del virtual_windows[file_name]
                        clicked = True
                        break

        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = None

    # Clear the screen
    screen.fill(WHITE)

    # Get mouse position
    x, y = pygame.mouse.get_pos()

    # Update positions if dragging
    if dragging:
        drag_type, drag_item = dragging
        if drag_type == 'square':
            positions[drag_item] = (x - 25, y - 25)
        elif drag_type == 'window':
            virtual_windows[drag_item] = (x - 100, y - 100)

    # Render squares and file names based on hover
    for file_name, (pos_x, pos_y) in positions.items():
        rect = pygame.Rect(pos_x, pos_y, 50, 50)
        pygame.draw.rect(screen, BLUE, rect, 2)
        if rect.collidepoint(x, y):
            text = font.render(file_name, True, BLACK)
            text_rect = text.get_rect(center = (pos_x + 25, pos_y + 25))
            screen.blit(text, text_rect)

    # Render virtual windows
    for file_name, (win_x, win_y) in virtual_windows.items():
        win_rect = pygame.Rect(win_x, win_y, 200, 200)
        close_rect = pygame.Rect(win_x + 180, win_y + 10, 10, 10)
        pygame.draw.rect(screen, BLACK, win_rect, 2)
        pygame.draw.rect(screen, RED, close_rect)
        pygame.draw.line(screen, WHITE, (win_x + 180, win_y + 10), (win_x + 190, win_y + 20))
        pygame.draw.line(screen, WHITE, (win_x + 190, win_y + 10), (win_x + 180, win_y + 20))
        # Render file content
        if file_content:
            y_offset = win_y  # Starting Y-position for rendering file content
            for idx, line in enumerate(file_content.split('\n')):
                content_text = font.render(line, True, BLACK)
                screen.blit(content_text, [300, y_offset + idx * 40])
 
    # Update the display
    pygame.display.update()

# Clean up
pygame.quit()
