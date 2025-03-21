import time
import pygame
import config
from grid import draw_grid


### NEED TO CHANGE THIS TO BE RECURSIVE ALGORITHM. THIS WAS JUST USED AS A TEST.


def dfs(maze, start_x, start_y, goal_x, goal_y, screen):
    stack = [(start_x, start_y)]  # Stack to hold positions
    visited = set()  # Set to track visited nodes

    total_cost = 0

    while stack:
        x, y = stack.pop()  # Get the current node

        # Skip if already visited
        if (x, y) in visited:
            continue
        visited.add((x, y))

        # Mark the current node as part of the path
        total_cost += maze[y][x].cost

        maze[y][x].cost = config.SEARCHED  # Change color or cost to show the AI path
        draw_grid(screen, maze)  # Redraw the grid with updated colors
        pygame.display.flip()  # Update the screen

        time.sleep(0.05)  # Small delay to make the animation visible

        # Check if goal is reached
        if x == goal_x and y == goal_y:
            print(f"Total Cost: {total_cost}")
            return True

        # Add neighboring nodes to the stack (up, down, left, right)
        if x > 0 and maze[y][x - 1].traversable:  # Left
            stack.append((x - 1, y))
        if x < len(maze[0]) - 1 and maze[y][x + 1].traversable:  # Right
            stack.append((x + 1, y))
        if y > 0 and maze[y - 1][x].traversable:  # Up
            stack.append((x, y - 1))
        if y < len(maze) - 1 and maze[y + 1][x].traversable:  # Down
            stack.append((x, y + 1))


    return False  # No path found
