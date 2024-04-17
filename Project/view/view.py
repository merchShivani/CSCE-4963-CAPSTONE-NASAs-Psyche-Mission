import pygame
import os
import time
from utils import get_project_root
from magField import magField1

class GameView:
    def __init__(self, model):
        self.model = model
        self.magfield_game = magField1()

        pygame.init()

        # Set your desired resolution
        game_width, game_height = 1920, 1080

        self.is_fullscreen = True  # Tracks the fullscreen state

        # Set the display mode to fullscreen with the specified game resolution
        self.screen = pygame.display.set_mode((game_width, game_height), pygame.FULLSCREEN)
        pygame.display.set_caption("Psyche")

        root = get_project_root()

        # Load multiple images from the "images" directory
        self.background = pygame.image.load(os.path.join(root, "project/assets/images/background.png"))
        self.psyche = pygame.image.load(os.path.join(root, "project/assets/images/psyche_asteroid.png"))
        self.psyche = pygame.transform.scale(self.psyche, (self.psyche.get_width() // 2, self.psyche.get_height() // 2))  # Scale the image to half size

        # Get the rectangle that encloses the scaled asteroid image
        self.psyche_rect = self.psyche.get_rect()

        # Initial angle for rotation
        self.angle = 0  

    def toggle_fullscreen(self):
        # Toggles fullscreen mode
        if self.is_fullscreen:
            self.screen = pygame.display.set_mode((self.game_width, self.game_height))
            self.is_fullscreen = False
        else:
            self.screen = pygame.display.set_mode((self.game_width, self.game_height), pygame.FULLSCREEN)
            self.is_fullscreen = True

    def draw_gammas_and_neutrons(self):
        if self.model.spectroGame_bool:
            for gamma in self.model.gammas:
                self.screen.blit(gamma.image, gamma.rect.topleft)
            for neutron in self.model.neutrons:
                self.screen.blit(neutron.image, neutron.rect.topleft)

    def update_display(self):
        if self.model.magfieldGame_bool == False:
            # Clear the screen
            self.screen.fill((255, 255, 255))  # Fill with black background
            self.screen.blit(self.background, (0, 0))

            # Calculate position to center the image of psyche and render
            psyche_x = (self.screen.get_width() - self.psyche.get_width()) // 2
            psyche_y = (self.screen.get_height() - self.psyche.get_height()) // 2
            
            # Get the center of the screen
            center = (self.screen.get_width() // 2, self.screen.get_height() // 2)
            
            # Rotate the asteroid image around the center of the screen
            rotated_psyche = pygame.transform.rotate(self.psyche, self.angle)
            rotated_rect = rotated_psyche.get_rect(center=center)
            
            self.screen.blit(rotated_psyche, rotated_rect.topleft)
            
            # Draw Psyche spacecraft
            self.screen.blit(self.model.psyche_spacecraft.image, self.model.psyche_spacecraft.rect.topleft)

            # Draw gammas and neutrons
            self.draw_gammas_and_neutrons()

            # Update the display
            pygame.display.flip()

            # Increment the rotation angle for the next frame (adjust rotation speed)
            self.angle += 0.1  # Adjust rotation speed as needed

        else:
            # Run the mini-game and pass the main display surface
            if self.magfield_game.create_mini_screen(self.screen):
                print("You've won the matching game!")
                self.model.magfieldGame_bool = False
            else:
                print("You've lost the matching game!")
                self.model.magfieldGame_bool = False
