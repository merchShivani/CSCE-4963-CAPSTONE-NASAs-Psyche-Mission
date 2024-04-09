import pygame
import os
import time
from utils import get_project_root

class GameView:
    def __init__(self, model):
        self.model = model

        pygame.init()

        # Set your desired resolution
        game_width, game_height = 1920, 1080

        # Set the display mode to fullscreen with the specified game resolution
        self.screen = pygame.display.set_mode((game_width, game_height), pygame.FULLSCREEN)
        pygame.display.set_caption("Psyche")

        root = get_project_root()

        # Load multiple images from the "images" directory
        self.background = pygame.image.load(os.path.join(root, "project/assets/images/background.png"))
        self.psyche = pygame.image.load(os.path.join(root, "project/assets/images/psyche_asteroid.png"))
        self.psyche = pygame.transform.scale(self.psyche, (self.psyche.get_width() // 2, self.psyche.get_height() // 2))  # Scale the image to half size


    def update_display(self):
        # Clear the screen
        self.screen.fill((255, 255, 255))  # Fill with black background
        self.screen.blit(self.background, (0, 0))

        # Calculate position to center the image of psyche and render
        psyche_x = (self.screen.get_width() - self.psyche.get_width()) // 2
        psyche_y = (self.screen.get_height() - self.psyche.get_height()) // 2
        self.screen.blit(self.psyche, (psyche_x, psyche_y))
        
        # Draw Psyche spacecraft
        self.screen.blit(self.model.psyche_spacecraft.image, self.model.psyche_spacecraft.rect.topleft)

        for gamma in self.model.gammas:
            self.screen.blit(gamma.image, gamma.rect.topleft)

        for neutron in self.model.neutrons:
            self.screen.blit(neutron.image, neutron.rect.topleft)

        # Update the display
        pygame.display.flip()