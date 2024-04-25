import pygame
from view.splash import splash
from view.menu import menu
from model.model import GameModel
from view.view import GameView
from controller.controller import GameController
from utils import get_project_root  # Import get_project_root
import os

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

    # Get display info
    info = pygame.display.Info()

    # Get fullscreen width and height
    game_width = info.current_w
    game_height = info.current_h

    #game_width, game_height = 1920, 1080
    root = get_project_root()
    # Set the display mode to fullscreen with the specified game resolution
    screen = pygame.display.set_mode((game_width, game_height), pygame.FULLSCREEN)
    pygame.display.set_caption("Mission to Psyche")
    music = pygame.mixer.music.load(os.path.join(root,'project/assets/Music/Music_Main_Theme.mp3'))
    pygame.mixer.music.play()
    splash(screen, game_width, game_height, pygame)
    menu(screen, game_width, game_height, pygame, main)