import pygame
from view.splash import splash
from view.menu import menu
from model.model import GameModel
from view.view import GameView
from controller.controller import GameController
from utils import get_project_root  # Import get_project_root

def main():
    model = GameModel()
    view = GameView(model)
    controller = GameController(model, view)

    while True:
        controller.handle_events()
        controller.update_model()
        view.update_display()
        model.handle_collisions()

if __name__ == "__main__":
    pygame.init()  # Initialize Pygame before anything else
    game_width, game_height = 1920, 1080
    # Set the display mode to fullscreen with the specified game resolution
    screen = pygame.display.set_mode((game_width, game_height), pygame.FULLSCREEN)
    pygame.display.set_caption("Mission to Psyche")

    splash(screen, game_width, game_height, pygame)
    menu(screen, game_width, game_height, pygame, main)