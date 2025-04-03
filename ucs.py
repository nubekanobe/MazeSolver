import time
import pygame
import config
import heapq
from grid import draw_grid


# UCS Implementation
def ucs(maze, start_x, start_y, goal_x, goal_y, screen):
    priority_queue = [(0, start_x, start_y)]  # (cost, x, y)
    visited = set()
    cost_so_far = {(start_x, start_y): 0}  # Track cost to reach each node

    while priority_queue:
        current_cost, x, y = heapq.heappop(priority_queue)  # Get the lowest-cost node

        # Skip if already visited
        if (x, y) in visited:
            continue
        visited.add((x, y))

        # Mark node as searched
        maze[y][x].cost = config.SEARCHED
        draw_grid(screen, maze)
        pygame.display.flip()
        time.sleep(0.05)  # Delay for visualization

        # Check if goal is reached
        if x == goal_x and y == goal_y:
            print(f"Total Cost: {current_cost}")
            return True

        # Explore neighbors with their respective costs
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze) and maze[ny][nx].traversable:
                new_cost = current_cost + maze[ny][nx].cost

                if (nx, ny) not in cost_so_far or new_cost < cost_so_far[(nx, ny)]:
                    cost_so_far[(nx, ny)] = new_cost
                    heapq.heappush(priority_queue, (new_cost, nx, ny))

    return False  # No path found
