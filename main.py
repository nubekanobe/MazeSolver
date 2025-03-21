import pygame
import sys
import config
import copy
import time
from grid import draw_grid
from maze import maze
from dfs import dfs

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


# Main game loop
def main():
    running = True
    path_found = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(config.WHITE)  # Clear the screen using WHITE color from config
        draw_grid(screen, maze)  # Draw the initial maze
        pygame.display.flip()  # Update the screen

        if not path_found:  # Only run the DFS if the path hasn't been found yet
            path_found = dfs(maze_copy, start_x, start_y, goal_x, goal_y, screen)
            if path_found:
                print("Path found!")
                time.sleep(4)
                path_found = True

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()



