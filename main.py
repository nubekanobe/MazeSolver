import pygame
import sys
import config
import copy
import time
from grid import draw_grid
from maze import maze1, maze2, maze3, GOAL_X, GOAL_Y
from dfs import dfs
from astar import astar
from ucs import ucs

pygame.init()

# Creating the window
# set_mode returns a Surface object that represents a windows display
# A Surface is where I can "draw things"
screen = pygame.display.set_mode((config.S_WIDTH, config.S_HEIGHT))
pygame.display.set_caption("Maze Solver")

maze_copy = copy.deepcopy(maze1)  # Creates a deep copy of the maze, this will be the default maze

start_x = 19
start_y = 19
goal_x = GOAL_X
goal_y = GOAL_Y

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
current_maze = maze_copy


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


# Run selected algorithm
def run_selected_algorithm():
    global output_message

    if selected_algorithm == 'DFS':
        path_found = dfs(maze_copy, start_x, start_y, goal_x, goal_y, screen)
    elif selected_algorithm == 'UCS':
        path_found = ucs(maze_copy, start_x, start_y, goal_x, goal_y, screen)
    elif selected_algorithm == 'A*':
        path_found = astar(maze_copy, start_x, start_y, goal_x, goal_y, screen)
    else:
        path_found = False

    output_message = f"{selected_algorithm}: Path found!" if path_found else f"{selected_algorithm}: No path found."

    if path_found:
        pygame.display.flip()
        time.sleep(3)  # Short delay before resetting
        reset_maze()


# Reset maze display
def reset_maze():
    global current_maze, output_message, maze_copy
    if selected_maze == "Maze 1":
        current_maze = copy.deepcopy(maze1)
    elif selected_maze == "Maze 2":
        current_maze = copy.deepcopy(maze2)
    elif selected_maze == "Maze 3":
        current_maze = copy.deepcopy(maze3)

    maze_copy = copy.deepcopy(current_maze)  # Ensure maze_copy is reset too
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

                        # Reset maze_copy correctly
                        if label == "Maze 1":
                            current_maze = copy.deepcopy(maze1)
                        elif label == "Maze 2":
                            current_maze = copy.deepcopy(maze2)
                        elif label == "Maze 3":
                            current_maze = copy.deepcopy(maze3)

                        reset_maze()  # Force reset to clean state

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
