import pygame
import sys
import os
from utils import get_project_root

from model.model import GameModel
from view.view import GameView
from controller.controller import GameController

def main():
    model = GameModel()
    view = GameView(model)
    controller = GameController(model, view)

    while True:
        controller.handle_events()
        controller.update_model()
        view.update_display()

pygame.init()

root = get_project_root()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)
BLACK = (0, 0, 0)

# Initialize Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mission to Psyche")

# Fonts
title_font = pygame.font.Font(None, 72)
button_font = pygame.font.Font(None, 36)

# Button properties
button_width, button_height = 200, 50
button_x, button_y = (WIDTH - button_width) // 2, HEIGHT // 2

# Create buttons with different colors
buttons = [
    {"text": "Start Journey", "action": "start_game", "color": GREEN},
    {"text": "Options", "action": "show_options", "color": ORANGE},
    {"text": "Quit", "action": "quit_game", "color": BLUE}
]

def draw_button(text, font, color, x, y, width, height):
    pygame.draw.rect(screen, color, (x, y, width, height))
    draw_text(text, font, BLACK, x + width // 2, y + height // 2)

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def splash_screen():
    # Load the image
    splash_image = pygame.image.load(os.path.join(root, "project/assets/images/splash.png"))

    # Calculate scaled dimensions while preserving aspect ratio
    original_width, original_height = splash_image.get_size()
    aspect_ratio = original_width / original_height

    # Determine the maximum scaled dimensions with padding
    max_scaled_width = WIDTH - 100  # Adjust the padding as needed
    max_scaled_height = HEIGHT - 100  # Adjust the padding as needed

    if aspect_ratio > (max_scaled_width / max_scaled_height):
        # Fit width to maximum scaled width
        scaled_width = max_scaled_width
        scaled_height = int(scaled_width / aspect_ratio)
    else:
        # Fit height to maximum scaled height
        scaled_height = max_scaled_height
        scaled_width = int(scaled_height * aspect_ratio)

    # Scale the image
    splash_image = pygame.transform.scale(splash_image, (scaled_width, scaled_height))

    # Center the image on the screen
    offset_x = (WIDTH - scaled_width) // 2
    offset_y = (HEIGHT - scaled_height) // 2

    # Blit the scaled image onto the screen
    screen.blit(splash_image, (offset_x, offset_y))

    # Update the display
    pygame.display.flip()

    # Wait for a moment
    pygame.time.delay(3000)  # Adjust the delay time as needed

def start_menu():

    splash_screen()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button["rect"].collidepoint(event.pos):
                        handle_button_action(button["action"])

        # Draw background
        screen.fill(BLACK)

        # Draw title
        draw_text("Mission to Psyche", title_font, BLUE, WIDTH // 2, HEIGHT // 4)

        # Draw buttons
        for button in buttons:
            button_color = button["color"] if button["rect"].collidepoint(pygame.mouse.get_pos()) else WHITE
            draw_button(button["text"], button_font, button_color, button["rect"].x, button["rect"].y, button_width, button_height)

        pygame.display.flip()
        pygame.time.Clock().tick(30)

def handle_button_action(action):
    if action == "start_game":
        print("Starting the game!")
        # Add your code to start the game here
        if __name__ == "__main__":
            main()
    elif action == "show_options":
        print("Opening options!")
        # Add your code to show options here
    elif action == "quit_game":
        pygame.quit()
        sys.exit()

# Create button rectangles
for i, button in enumerate(buttons):
    button["rect"] = pygame.Rect(button_x, button_y + i * (button_height + 10), button_width, button_height)

# Run the start menu
start_menu()

if __name__ == "__main__":
    main()
