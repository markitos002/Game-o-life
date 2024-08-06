import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 1000
HEIGHT = 1000
CELL_SIZE = 10
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255 , 255)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game of Life")

# Initialize grid
grid = np.zeros((GRID_HEIGHT, GRID_WIDTH))

# Function to update the grid
def update_grid(grid):
    new_grid = np.copy(grid)
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            alive_neighbors = np.sum(grid[row-1:row+2, col-1:col+2]) - grid[row, col]
            if grid[row, col] == 1:  # Alive
                if alive_neighbors < 2 or alive_neighbors > 3:
                    new_grid[row, col] = 0  # Dies
            else:  # Dead
                if alive_neighbors == 3:
                    new_grid[row, col] = 1  # Becomes alive
    return new_grid

# Function to draw the grid
def draw_grid(screen, grid):
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            color = WHITE if grid[row, col] == 1 else BLACK
            pygame.draw.rect(screen, color, (col*CELL_SIZE, row*CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Main loop
running = True
paused = False
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            grid[y // CELL_SIZE, x // CELL_SIZE] = 1 - grid[y // CELL_SIZE, x // CELL_SIZE]
    
    if not paused:
        grid = update_grid(grid)
    
    screen.fill(BLACK)
    draw_grid(screen, grid)
    pygame.display.flip()
    clock.tick(10)

pygame.quit()