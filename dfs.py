import time
import pygame
import config
from grid import draw_grid


def dfs(maze, start_x, start_y, goal_x, goal_y, screen):

    stack = [(start_x, start_y)]  # Initialize the stack with my start coordinates
    total_cost = 0
    nodes_explored = 0

    max_x = len(maze[0]) - 1    # max x-axis boundary
    max_y = len(maze) - 1   # max y-axis boundary
    min_x = 0   # min x_axis boundary
    min_y = 0   # min y_axis boundary

    while len(stack) > 0:
        current_node = stack.pop()
        curr_x, curr_y = current_node

        if maze[curr_y][curr_x].cost == config.SEARCHED:  # skip searched nodes
            continue

        total_cost += maze[curr_y][curr_x].cost
        nodes_explored += 1
        maze[curr_y][curr_x].cost = config.SEARCHED  # Change status to show the AI path

        draw_grid(screen, maze)  # Redraw the grid with updated colors
        pygame.display.flip()  # Update the screen
        time.sleep(0.05)

        if curr_x == goal_x and curr_y == goal_y:
            print(f"=== DFS Results ===")
            print(f"Nodes Explored: {nodes_explored}")
            print(f"Total Cost: {total_cost}")
            print(f"=====================")
            return True

        # Add neighboring nodes
        # Checks if we are currently at an edge
        if curr_x > min_x and maze[curr_y][curr_x - 1].traversable:  # Left neighbor
            stack.append((curr_x - 1, curr_y))
        if curr_x < max_x and maze[curr_y][curr_x + 1].traversable:  # Right neighbor
            stack.append((curr_x + 1, curr_y))
        if curr_y > min_y and maze[curr_y - 1][curr_x].traversable:  # Up neighbor
            stack.append((curr_x, curr_y - 1))
        if curr_y < max_y and maze[curr_y + 1][curr_x].traversable:  # Down neighbor
            stack.append((curr_x, curr_y + 1))

    print(f"=== DFS Results ===")
    print(f"Nodes Explored: {nodes_explored}")
    print(f"Total Cost: {total_cost}")
    print(f"=====================")
    return False  # No path found
