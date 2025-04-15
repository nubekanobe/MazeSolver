import time
import pygame
import config
from grid import draw_grid


def dfs(maze, start_x, start_y, goal_x, goal_y, screen):

    stack = [(start_x, start_y)]  # Initialize the stack with my start coordinates
    total_cost = 0
    nodes_explored = 0
    parent_of = {}   # This is used to recreate the [suboptimal] path found by DFS

    max_x = len(maze[0]) - 1    # max x-axis boundary
    max_y = len(maze) - 1   # max y-axis boundary
    min_x = 0   # min x_axis boundary
    min_y = 0   # min y_axis boundary

    while len(stack) > 0:
        current_node = stack.pop()
        curr_x, curr_y = current_node

        if maze[curr_y][curr_x].searched:  # skip searched nodes
            continue

        total_cost += maze[curr_y][curr_x].cost
        nodes_explored += 1
        maze[curr_y][curr_x].searched = True  # Change status to show the AI path

        draw_grid(screen, maze, start_x, start_y)  # Redraw the grid with updated colors
        pygame.display.flip()  # Update the screen
        time.sleep(0.03)

        if curr_x == goal_x and curr_y == goal_y:

            found_path = []
            current_node = (goal_x, goal_y)
            found_path_cost = 0

            while current_node != (start_x, start_y):
                found_path.append(current_node)
                curr_x, curr_y = current_node
                found_path_cost += maze[curr_y][curr_x].cost
                current_node = parent_of.get(current_node)
                if current_node is None:
                    break

            found_path_cost += maze[start_y][start_x].cost

            for x, y in reversed(found_path):
                maze[y][x].in_path = True
                draw_grid(screen, maze, start_x, start_y)
                pygame.display.flip()
                time.sleep(0.02)

            print(f"=== DFS Results ===")
            print(f"Nodes Explored: {nodes_explored}")
            print(f"Total Cost of Explored Nodes: {total_cost}")
            print(f"Total Nodes in Found Path: {len(found_path)}")
            print(f"Total Cost in Found Path: {found_path_cost}")
            print(f"=====================")
            return True, list(reversed(found_path))

        # Add neighboring nodes
        # Checks if we are currently at an edge
        # Tracks each node's parent and stores it in a dictionary
        if curr_x > min_x:
            left = (curr_x - 1, curr_y)
            if maze[left[1]][left[0]].traversable and left not in parent_of:
                stack.append(left)
                parent_of[left] = (curr_x, curr_y)

        if curr_x < max_x:
            right = (curr_x + 1, curr_y)
            if maze[right[1]][right[0]].traversable and right not in parent_of:
                stack.append(right)
                parent_of[right] = (curr_x, curr_y)

        if curr_y > min_y:
            up = (curr_x, curr_y - 1)
            if maze[up[1]][up[0]].traversable and up not in parent_of:
                stack.append(up)
                parent_of[up] = (curr_x, curr_y)

        if curr_y < max_y:
            down = (curr_x, curr_y + 1)
            if maze[down[1]][down[0]].traversable and down not in parent_of:
                stack.append(down)
                parent_of[down] = (curr_x, curr_y)

    print(f"=== DFS Results ===")
    print(f"No path found")
    print(f"Nodes Explored: {nodes_explored}")
    print(f"Total Cost: {total_cost}")
    print(f"=====================")
    return False  # No path found
