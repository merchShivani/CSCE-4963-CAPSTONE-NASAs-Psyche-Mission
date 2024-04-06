import pygame
from .sprites import PsycheSpacecraft, GammaRay, Neutrons
# import sys
# print(sys.path)

class GameModel:
    def __init__(self):
        # Initialize your model state and variables
        #self.object = []  # List to store spawned units
        self.dest_x = 0
        self.dest_y = 0
        self.sprites = []
        
        # Create player and Psyche spacecraft
        self.psyche_spacecraft = PsycheSpacecraft(800, 500)
        self.gammas = GammaRay(200, 700)
        self.neutrons = [Neutrons(100, 900)]

        # Define orbit parameters
        self.orbit_center = (1920 // 2, 1080 // 2)  # Center of the screen
        self.orbit_radius = 400  # Radius of the orbit
        self.orbit_speed = 0.3  # Speed of orbit in degrees/frame
        
        # Spectroscropy Game parameters
        self.captured_gammas = 0
        self.captured_neutrons = 0

        # Spectroscopy minigame toggle
        self.spectroGame_bool = False

    def update(self):
            # Update model state based on user input or other factors
            self.psyche_spacecraft.update_orbit(self.orbit_center, self.orbit_radius, self.orbit_speed)
            self.gammas.update_position(90, 80, 1920, 1080)

            # Spectroscopy Game
            if self.spectroGame_bool == True:
                 self.spectroGame()
            if ((self.captured_gammas == 5) and (self.captured_neutrons == 5)):
                 self.spectroGame_bool = False

    def spectroGame(self):
        self.captured_gammas = 0
        self.captured_neutrons = 0