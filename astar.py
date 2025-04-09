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
        draw_grid(screen, maze)
        pygame.display.flip()
        time.sleep(0.05)

        if x == goal_x and y == goal_y:
            # Reconstruct path
            path = []
            cx, cy = x, y
            total_path_cost = 0

            while (cx, cy) != (start_x, start_y):
                path.append((cx, cy))
                prev = came_from[(cx, cy)]
                step_cost = cost_so_far[(cx, cy)] - cost_so_far[prev]
                total_path_cost += step_cost
                cx, cy = prev

            path.append((start_x, start_y))

            # Highlight path
            for px, py in reversed(path):
                maze[py][px].cost = config.BEST
                draw_grid(screen, maze)
                pygame.display.flip()
                time.sleep(0.02)

            print(f"=== A Star Results ===")
            print(f"Total Nodes Explored: {explored_count}")
            print(f"Total Cost of Explored Nodes: {explored_cost}")
            print(f"Total Nodes in Best Path: {len(path)}")
            print(f"Total Cost of Best Path: {total_path_cost}")
            print(f"=====================")
            return True

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
