import pygame
import config
from maze import GOAL_X
from maze import GOAL_Y


def draw_grid(screen, maze, start_x, start_y, algorithm):
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            node = maze[y][x]  # Point to the current MazeNode object in the loop

            color = config.GRAY

            # Determine the nodes color based on its properties
            if node.x == GOAL_X and node.y == GOAL_Y:
                color = config.RED  # Goal node
            elif node.x == start_x and node.y == start_y:
                color = config.ORANGE   # Start node
            elif node.in_path:
                if algorithm in ("A*", "UCS"):
                    color = config.YELLOW
                elif algorithm == "DFS":
                    color = config.MAGENTA
            elif node.searched:
                color = config.PURPLE
            elif not node.traversable:  # Walls
                color = config.BLACK
            elif node.cost == config.WATER:
                color = config.BLUE
            elif node.cost == config.BRIDGE:
                color = config.BROWN
            elif node.cost == config.GRASS:
                color = config.GREEN
            else:
                color = config.GRAY  # Normal traversable paths

            # This draws one square for each iteration of the loop
            pygame.draw.rect(
                screen,
                color,
                (x * config.GRID_SIZE, y * config.GRID_SIZE, config.GRID_SIZE, config.GRID_SIZE),
            )

            # We only use this to show grid lines to assist with modifying the maze
            '''
            pygame.draw.rect(
                screen,
                config.GRAY,  # Grid lines
                (x * config.GRID_SIZE, y * config.GRID_SIZE, config.GRID_SIZE, config.GRID_SIZE),
                1,
            )
            '''