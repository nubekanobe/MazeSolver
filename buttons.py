import pygame
import config
from config import *

button_height = 30
button_width = 90
button_spacing = 10
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

def draw_rounded_button(screen, rect, label, font, selected=False):
    color = (200, 200, 200) if not selected else (160, 160, 160)
    pygame.draw.rect(screen, color, rect, border_radius=6)
    pygame.draw.rect(screen, config.BLACK, rect, 2, border_radius=6)
    text = font.render(label, True, config.BLACK)
    text_rect = text.get_rect(center=rect.center)
    screen.blit(text, text_rect)

def draw_buttons(screen, selected_algorithm, selected_maze, output_message):
    font = get_font(20)
    font_small = get_font(18)

    for label, rect in algo_buttons.items():
        draw_rounded_button(screen, rect, label, font, selected_algorithm == label)

    for label, rect in maze_buttons.items():
        draw_rounded_button(screen, rect, label, font, selected_maze == label)

    draw_rounded_button(screen, run_button, "Run", font)
    draw_rounded_button(screen, reset_button, "Reset", font)

    pygame.draw.rect(screen, config.WHITE, output_box, border_radius=6)
    pygame.draw.rect(screen, config.BLACK, output_box, 2, border_radius=6)
    output_text = font_small.render(output_message, True, config.BLACK)
    screen.blit(output_text, (output_box.x + 8, output_box.y + 5))
