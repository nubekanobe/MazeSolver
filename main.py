import pygame
import sys
import config
import copy
import time
from grid import draw_grid
from maze import maze, maze_layout1, MazeNode, maze_layout2, maze_layout3
from dfs import dfs
from collections import deque
import heapq

pygame.init()

# Creating the window
# set_mode returns a Surface object that represents a windows display
# A Surface is where I can "draw things"
screen = pygame.display.set_mode((config.S_WIDTH, config.S_HEIGHT))
pygame.display.set_caption("Maze Solver")

maze_copy = copy.deepcopy(maze)  # Creates a deep copy of the maze

start_x = 19
start_y = 19
goal_x = 1
goal_y = 1

# UI Components
font = pygame.font.SysFont("Segoe UI", 20)

# Buttons
button_height = 30
button_width = 90
button_spacing = 10

# Button layout positions
x1, x2 = 480, 580
start_y_pos = 30

algo_buttons = {
    "DFS": pygame.Rect(x1, start_y_pos, button_width, button_height),
    "UCS": pygame.Rect(x2, start_y_pos, button_width, button_height),
    "A*": pygame.Rect(x1, start_y_pos + button_height + button_spacing, button_width, button_height),
}

maze_buttons = {
    "Maze 1": pygame.Rect(x2, start_y_pos + button_height + button_spacing, button_width, button_height),
    "Maze 2": pygame.Rect(x1, start_y_pos + 2 * (button_height + button_spacing), button_width, button_height),
    "Maze 3": pygame.Rect(x2, start_y_pos + 2 * (button_height + button_spacing), button_width, button_height),
}

run_button = pygame.Rect(x1, start_y_pos + 3 * (button_height + button_spacing), 190, button_height)
reset_button = pygame.Rect(x1, start_y_pos + 4 * (button_height + button_spacing), 190, button_height)
output_box = pygame.Rect(x1, start_y_pos + 5 * (button_height + button_spacing), 190, button_height)

selected_algorithm = 'DFS'
selected_maze = 'Maze 1'
output_message = ''
current_maze = maze

# Function to draw rounded rectangles
def draw_rounded_button(rect, label, selected=False):
    color = (200, 200, 200) if not selected else (160, 160, 160)
    pygame.draw.rect(screen, color, rect, border_radius=6)
    pygame.draw.rect(screen, config.BLACK, rect, 2, border_radius=6)
    text = font.render(label, True, config.BLACK)
    text_rect = text.get_rect(center=rect.center)
    screen.blit(text, text_rect)

# Function to draw all buttons and output box
def draw_buttons():
    for label, rect in algo_buttons.items():
        draw_rounded_button(rect, label, selected_algorithm == label)

    for label, rect in maze_buttons.items():
        draw_rounded_button(rect, label, selected_maze == label)

    draw_rounded_button(run_button, "Run")
    draw_rounded_button(reset_button, "Reset")

    pygame.draw.rect(screen, config.WHITE, output_box, border_radius=6)
    pygame.draw.rect(screen, config.BLACK, output_box, 2, border_radius=6)
    output_text = font.render(output_message, True, config.BLACK)
    screen.blit(output_text, (output_box.x + 8, output_box.y + 5))

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

# Run selected algorithm
def run_selected_algorithm():
    global output_message
    maze_copy = copy.deepcopy(current_maze)

    if selected_algorithm == 'DFS':
        path_found = dfs(maze_copy, start_x, start_y, goal_x, goal_y, screen)
    elif selected_algorithm == 'UCS':
        path_found = ucs(maze_copy, start_x, start_y, goal_x, goal_y, screen)
    elif selected_algorithm == 'A*':
        path_found = astar(maze_copy, start_x, start_y, goal_x, goal_y, screen)
    else:
        path_found = False

    output_message = f"{selected_algorithm}: Path found!" if path_found else f"{selected_algorithm}: No path found."

# Reset maze display
def reset_maze():
    global current_maze, output_message
    current_maze = copy.deepcopy(maze)
    output_message = "Maze reset."

# Main game loop
def main():
    global selected_algorithm, selected_maze, output_message, current_maze

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()

                for label, rect in algo_buttons.items():
                    if rect.collidepoint((mx, my)):
                        selected_algorithm = label
                        output_message = f"{label} selected."

                for label, rect in maze_buttons.items():
                    if rect.collidepoint((mx, my)):
                        selected_maze = label
                        output_message = f"{label} selected."

                        if label == "Maze 1":
                            current_maze = [
                                [MazeNode(x, y, traversable=(maze_layout1[y][x] != config.WALL), cost=maze_layout1[y][x])
                                 for x in range(len(maze_layout1[0]))] for y in range(len(maze_layout1))]
                        elif label == "Maze 2":
                            current_maze = [
                                [MazeNode(x, y, traversable=(maze_layout2[y][x] != config.WALL), cost=maze_layout2[y][x])
                                 for x in range(len(maze_layout2[0]))] for y in range(len(maze_layout2))]
                        elif label == "Maze 3":
                            current_maze = [
                                [MazeNode(x, y, traversable=(maze_layout3[y][x] != config.WALL), cost=maze_layout3[y][x])
                                 for x in range(len(maze_layout3[0]))] for y in range(len(maze_layout3))]

                if run_button.collidepoint((mx, my)):
                    run_selected_algorithm()

                if reset_button.collidepoint((mx, my)):
                    reset_maze()

        screen.fill(config.WHITE)
        draw_grid(screen, current_maze)
        draw_buttons()
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()