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
        self.gammas = [GammaRay(200, 700) for _ in range(5)]
        self.neutrons = [Neutrons(200, 700) for _ in range(5)]

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

            # Spectroscopy Game
            if self.spectroGame_bool == True:
                 self.spectroGame()
            if ((self.captured_gammas == 5) and (self.captured_neutrons == 5)):
                 self.spectroGame_bool = False
                 print("Captured all")


    def handle_collisions(self):
        if self.spectroGame_bool == True:
        # Handle GammaRay collisions
            for gamma in self.gammas[:]:  # Iterate over a copy of the list
                if self.psyche_spacecraft.check_collision(gamma):
                    self.gammas.remove(gamma)  # Remove the collided gamma
                    # Increment captured_gammas or handle as needed
                    self.captured_gammas = self.captured_gammas + 1
                    if self.captured_gammas == 1:
                        print(self.captured_gammas, "gamma")
                    else:
                        print(self.captured_gammas, "gammas")
            # Handle Neutron collisions
            for neutron in self.neutrons[:]:  # Iterate over a copy of the list
                if self.psyche_spacecraft.check_collision(neutron):
                    self.neutrons.remove(neutron)  # Remove the collided neutron
                    # Increment captured_neutrons or handle as needed
                    self.captured_neutrons = self.captured_neutrons + 1
                    if self.captured_neutrons == 1:
                        print(self.captured_neutrons, "neutron")
                    else:
                        print(self.captured_neutrons, "neutrons")

    def spectroGame(self):
        #self.captured_gammas = 0
        #self.captured_neutrons = 0
        for gamma in self.gammas:
            gamma.update_position(960, 540, 1920, 1080)
        for neutron in self.neutrons:
            neutron.update_position(960, 540, 1920, 1080)