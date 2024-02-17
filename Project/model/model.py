import pygame
from .sprites import Player, PsycheSpacecraft
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
        self.player = Player(100, 500)
        self.psyche_spacecraft = PsycheSpacecraft(800, 500)

        # Define orbit parameters
        self.orbit_center = (1920 // 2, 1080 // 2)  # Center of the screen
        self.orbit_radius = 400  # Radius of the orbit
        self.orbit_speed = 0.3  # Speed of orbit in degrees/frame

    def update(self):
            # Update model state based on user input or other factors
            self.psyche_spacecraft.update_orbit(self.orbit_center, self.orbit_radius, self.orbit_speed)