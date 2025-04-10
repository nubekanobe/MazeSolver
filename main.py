import pygame
import sys
import config
import copy
import time

from grid import draw_grid
from maze import maze1, maze2, maze3, START_X, START_Y, GOAL_X, GOAL_Y
from dfs import dfs
from astar import astar
from ucs import ucs

from buttons import (draw_buttons, algo_buttons, maze_buttons, run_button, reset_button)

pygame.init()

# Create window
screen = pygame.display.set_mode((config.S_WIDTH, config.S_HEIGHT))
pygame.display.set_caption("Maze Solver")

# Coordinates for start and goal
start_x, start_y = START_X, START_Y
goal_x, goal_y = GOAL_X, GOAL_Y

# Maze and state variables
current_maze = copy.deepcopy(maze1)
maze_copy = copy.deepcopy(current_maze)
selected_algorithm = 'DFS'
selected_maze = 'Maze 1'
output_message = ''


def run_selected_algorithm():
    global output_message, maze_copy

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

    if path_found:
        output_message = f"{selected_algorithm}: Path found!"

    else:
        width, height = screen.get_size()
        red = (255, 0, 0)

        pygame.draw.line(screen, red, (0, 0), (width, height), 10)
        pygame.draw.line(screen, red, (0, height), (width, 0), 10)

        pygame.display.flip()  # display x
        time.sleep(2)  # Display for 2 seconds
        reset_maze(f"{selected_algorithm}: No path found.")


def reset_maze(msg=None):
    global current_maze, maze_copy, output_message

    if selected_maze == "Maze 1":
        current_maze = copy.deepcopy(maze1)
    elif selected_maze == "Maze 2":
        current_maze = copy.deepcopy(maze2)
    elif selected_maze == "Maze 3":
        current_maze = copy.deepcopy(maze3)

    maze_copy = copy.deepcopy(current_maze)
    output_message = "Maze reset."

    if msg:
        output_message = msg


def main():
    global selected_algorithm, selected_maze, output_message, current_maze, maze_copy

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()

                for label, rect in algo_buttons.items():
                    if rect.collidepoint((mx, my)) and selected_algorithm != label:
                        selected_algorithm = label
                        output_message = f"{label} selected."
                        reset_maze(f"{label} selected.")

                for label, rect in maze_buttons.items():
                    if rect.collidepoint((mx, my)):
                        selected_maze = label
                        output_message = f"{label} selected."
                        reset_maze(f"{label} selected.")

                if run_button.collidepoint((mx, my)):
                    run_selected_algorithm()

                if reset_button.collidepoint((mx, my)):
                    reset_maze("Maze Reset")

        screen.fill(config.WHITE)
        draw_grid(screen, maze_copy)
        draw_buttons(screen, selected_algorithm, selected_maze, output_message)
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
