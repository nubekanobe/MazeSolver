import pygame
import config
from maze import GOAL_X
from maze import GOAL_Y


def draw_grid(screen, maze):
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            node = maze[y][x]  # Point to the current MazeNode object in the loop

            # Determine color based on node properties
            if node.x == GOAL_X and node.y == GOAL_Y:
                color = config.RED  # Goal node
            elif not node.traversable:
                color = config.BLACK  # Walls
            elif node.cost == config.WATER:
                color = config.BLUE
            elif node.cost == config.BRIDGE:
                color = config.BROWN
            elif node.cost == config.MUD:
                color = config.GREEN
            elif node.cost == config.SEARCHED:
                color = config.PURPLE
            else:
                color = config.GRAY  # Normal traversable paths

            # Drawing one square at a time for this loop
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
# Test