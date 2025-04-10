import pygame
import config
from maze import GOAL_X
from maze import GOAL_Y
from maze import START_X
from maze import START_Y


def draw_grid(screen, maze):
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            node = maze[y][x]  # Point to the current MazeNode object in the loop

            # Determine the nodes color based on its properties
            if node.x == GOAL_X and node.y == GOAL_Y:
                color = config.RED  # Goal node
            elif node.x == START_X and node.y == START_Y:
                color = config.ORANGE # Start node
            elif not node.traversable:  # Walls
                color = config.BLACK
            elif node.cost == config.WATER:
                color = config.BLUE
            elif node.cost == config.BRIDGE:
                color = config.BROWN
            elif node.cost == config.GRASS:
                color = config.GREEN
            elif node.cost == config.SEARCHED:
                color = config.PURPLE
            elif node.cost == config.BEST:
                color = config.YELLOW
            else:
                color = config.GRAY  # Normal traversable paths

            # This draws one square for each iteration of the loop
            pygame.draw.rect(
                screen,
                color,
                (x * config.GRID_SIZE, y * config.GRID_SIZE, config.GRID_SIZE, config.GRID_SIZE),
            )

            # We only use this to help modify the maze
            '''
            pygame.draw.rect(
                screen,
                config.GRAY,  # Grid lines
                (x * config.GRID_SIZE, y * config.GRID_SIZE, config.GRID_SIZE, config.GRID_SIZE),
                1,
            )
            '''