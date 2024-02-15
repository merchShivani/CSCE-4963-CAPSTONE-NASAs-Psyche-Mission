import pygame
import sys

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

def start_menu():
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
        draw_text("Colored Cartoon Adventure", title_font, BLUE, WIDTH // 2, HEIGHT // 4)

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
