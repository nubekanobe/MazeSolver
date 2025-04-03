import time
import pygame
import config
import heapq
from grid import draw_grid


# A* Implementation
def astar(maze, start_x, start_y, goal_x, goal_y, screen):
    open_set = [(0 + maze[start_y][start_x].heuristic, 0, start_x, start_y)]
    cost_so_far = {(start_x, start_y): 0}
    visited = set()

    while open_set:
        _, cost, x, y = heapq.heappop(open_set)

        if (x, y) in visited:
            continue
        print(f"Visiting ({x}, {y}) with terrain cost: {maze[y][x].cost}")
        maze[y][x].cost = config.SEARCHED
        visited.add((x, y))
        maze[y][x].cost = config.SEARCHED

        draw_grid(screen, maze)
        pygame.display.flip()
        time.sleep(0.05)

        if x == goal_x and y == goal_y:
            print(f"Total Cost: {cost}")
            return True

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze):
                neighbor = maze[ny][nx]
                if neighbor.traversable:
                    new_cost = cost + neighbor.cost
                    if (nx, ny) not in cost_so_far or new_cost < cost_so_far[(nx, ny)]:
                        cost_so_far[(nx, ny)] = new_cost
                        h = neighbor.heuristic
                        heapq.heappush(open_set, (new_cost + h, new_cost, nx, ny))

    return False
