import time
import pygame
import config
import heapq
from grid import draw_grid


def ucs(maze, start_x, start_y, goal_x, goal_y, screen):
    priority_queue = [(0, start_x, start_y)]
    cost_so_far = {(start_x, start_y): 0}
    came_from = {}

    explored_count = 0
    explored_cost = 0

    while priority_queue:
        current_cost, x, y = heapq.heappop(priority_queue)

        if maze[y][x].searched:
            continue
        maze[y][x].searched = True

        explored_count += 1
        explored_cost += maze[y][x].cost

        maze[y][x].searched = True
        draw_grid(screen, maze, start_x, start_y, "UCS")
        pygame.display.flip()
        time.sleep(0.03)

        if x == goal_x and y == goal_y:
            # Once we've reached the goal, we use our
            # came_from dictionary to backtrack until
            # we reach the start, adding each node along
            # the way to our path list
            optimal_path = []
            curr_x, curr_y = x, y
            total_path_cost = cost_so_far[(goal_x, goal_y)]

            while (curr_x, curr_y) != (start_x, start_y):
                optimal_path.append((curr_x, curr_y))
                prev_node = came_from[(curr_x, curr_y)]
                curr_x, curr_y = prev_node

            optimal_path.append((start_x, start_y))

            # Highlight the optimal path
            for optimal_x, optimal_y in reversed(optimal_path):
                maze[optimal_y][optimal_x].in_path = True
                draw_grid(screen, maze, start_x, start_y, "UCS")
                pygame.display.flip()
                time.sleep(0.02)

            print(f"=== UCS Results ===")
            print(f"Total Nodes Explored: {explored_count}")
            print(f"Total Cost of Explored Nodes: {explored_cost}")
            print(f"Total Nodes in Best Path: {len(optimal_path)}")
            print(f"Total Cost of Best Path: {total_path_cost}")
            print(f"=====================")

            return True, list(reversed(optimal_path))

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze) and maze[ny][nx].traversable:
                new_cost = current_cost + maze[ny][nx].cost

                if (nx, ny) not in cost_so_far or new_cost < cost_so_far[(nx, ny)]:
                    cost_so_far[(nx, ny)] = new_cost
                    came_from[(nx, ny)] = (x, y)
                    heapq.heappush(priority_queue, (new_cost, nx, ny))

    print(f"=== UCS Results ===")
    print("No path found.")
    print(f"Total Nodes Explored: {explored_count}")
    print(f"Total Cost of Explored Nodes: {explored_cost}")
    print(f"=====================")

    return False, []
