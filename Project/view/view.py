import pygame
import math

class GameView:
    def __init__(self, model):
        self.model = model

        pygame.init()

        # Set your desired resolution
        game_width, game_height = 1920, 1080

        # Set the display mode to fullscreen with the specified game resolution
        self.screen = pygame.display.set_mode((game_width, game_height), pygame.FULLSCREEN)
        pygame.display.set_caption("Psyche")

        # Load multiple images from the "images" directory
        self.space_backgroud = pygame.image.load("space.png")
        self.space_background_width = self.space_backgroud.get_width()

        # Define game variables 
        self.tiles = math.ceil(game_width / self.space_background_width)
        # Scale the images to the desired size
        
        # Get the rects of the images for positioning


        # Define positions for each image


    def update_display(self):
        #self.screen.fill((0, 0, 0))  # Fill with black background
        for i in range (0, 2):
            self.screen.blit(self.space_backgroud,(i * self.space_background_width, 0))

        # Update the display
        pygame.display.flip()
