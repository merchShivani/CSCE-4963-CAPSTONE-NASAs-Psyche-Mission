import pygame
from sprites import Player, PsycheSpacecraft

class GameModel:
    def __init__(self):
        # Initialize your model state and variables
        #self.object = []  # List to store spawned units
        self.dest_x = 0
        self.dest_y = 0
        self.sprites = []
        
        self.player = Player(100, 500)  # Adjust initial position as needed
        self.psyche_spacecraft = PsycheSpacecraft(800, 500)  # Adjust initial position as needed

        def update(self):
        # Update model state based on user input or other factors
            pass
