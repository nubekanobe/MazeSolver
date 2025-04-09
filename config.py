# config.py

# Defining the window dimensions
S_WIDTH, S_HEIGHT = 700, 415


# Setting up the grid
GRID_SIZE = 20

# Defining Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BROWN = (139, 69, 19)
GREEN = (0, 255, 0)
PURPLE = (128, 0, 128)
YELLOW = (255, 255, 0)


# Terrain Types With Costs
WALL = 0
PATH = 1
BRIDGE = 2
GRASS = 20
WATER = 100
SEARCHED = -1
BEST = -2

#Font
import pygame

def get_font(size):
    return pygame.font.SysFont("Arial", size)