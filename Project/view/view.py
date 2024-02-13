import pygame
import os


class GameView:
    def __init__(self, model):
        self.model = model

        pygame.init()

        # Set your desired resolution
        game_width, game_height = 1920, 1080

        # Set the display mode to fullscreen with the specified game resolution
        self.screen = pygame.display.set_mode((game_width, game_height), pygame.FULLSCREEN)
        pygame.display.set_caption("Psyche")

        # Change the working directory to where your assets folder is located
        os.chdir("C:\\Psyche\\Psyche2\\Project")  # Change this to the correct path

        # Load multiple images from the "images" directory
        self.background = pygame.image.load(os.path.join("assets\\images", "background.png"))


    def update_display(self):
        # Clear the screen
        self.screen.fill((255, 255, 255))  # Fill with black background
        self.screen.blit(self.background, (0, 0))

        # Draw player and Psyche spacecraft
        self.screen.blit(self.model.player.image, self.model.player.rect.topleft)
        self.screen.blit(self.model.psyche_spacecraft.image, self.model.psyche_spacecraft.rect.topleft)

        # Update the display
        pygame.display.flip()
