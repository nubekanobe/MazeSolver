import time
import pygame
import config
import heapq
from grid import draw_grid


def astar(maze, start_x, start_y, goal_x, goal_y, screen):
    open_set = [(0 + maze[start_y][start_x].heuristic, 0, start_x, start_y)]
    cost_so_far = {(start_x, start_y): 0}
    came_from = {}
    visited = set()

    explored_count = 0
    explored_cost = 0

    while open_set:
        _, cost, x, y = heapq.heappop(open_set)

        if (x, y) in visited:
            continue
        visited.add((x, y))

        explored_count += 1
        explored_cost += maze[y][x].cost

        maze[y][x].cost = config.SEARCHED
        draw_grid(screen, maze, start_x, start_y)
        pygame.display.flip()
        time.sleep(0.03)

        if x == goal_x and y == goal_y:
            # Once we've reached the goal, we use our
            # came_from dictionary to backtrack until
            # we reach the start, adding each node along
            # the way to our path list
            path = []
            curr_x, curr_y = x, y
            total_path_cost = cost_so_far[(goal_x, goal_y)]

            while (curr_x, curr_y) != (start_x, start_y):
                path.append((curr_x, curr_y))
                prev = came_from[(curr_x, curr_y)]
                curr_x, curr_y = prev

            path.append((start_x, start_y))

            # Highlight the optimal path
            for optimal_x, optimal_y in reversed(path):
                maze[optimal_y][optimal_x].cost = config.BEST
                draw_grid(screen, maze, start_x, start_y)
                pygame.display.flip()
                time.sleep(0.02)

            print(f"=== A Star Results ===")
            print(f"Total Nodes Explored: {explored_count}")
            print(f"Total Cost of Explored Nodes: {explored_cost}")
            print(f"Total Nodes in Best Path: {len(path)}")
            print(f"Total Cost of Best Path: {total_path_cost}")
            print(f"=====================")
            return True, list(reversed(path))

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze):
                neighbor = maze[ny][nx]
                if neighbor.traversable:
                    new_cost = cost + neighbor.cost
                    if (nx, ny) not in cost_so_far or new_cost < cost_so_far[(nx, ny)]:
                        cost_so_far[(nx, ny)] = new_cost
                        came_from[(nx, ny)] = (x, y)
                        priority = new_cost + neighbor.heuristic
                        heapq.heappush(open_set, (priority, new_cost, nx, ny))

    print(f"=== A Star Results ===")
    print("No path found.")
    print(f"Total Nodes Explored: {explored_count}")
    print(f"Total Cost of Explored Nodes: {explored_cost}")
    print(f"=====================")
    return False
