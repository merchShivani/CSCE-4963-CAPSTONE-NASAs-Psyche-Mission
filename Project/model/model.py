import pygame
import random
import time
from pygame.locals import USEREVENT
from .sprites import PsycheSpacecraft, GammaRay, Neutrons
from magField import magField1

class GameModel:
    def __init__(self):
        # Initialize your model state and variables
        self.dest_x = 0
        self.dest_y = 0
        self.sprites = []

        # Instantiate Magfield Game
        self.magfield_game = magField1()

        # Capture Game Data
        self.captures = 0
        
        # Create player and Psyche spacecraft
        self.psyche_spacecraft = PsycheSpacecraft(800, 500)

        # Initialize lists for gammas and neutrons
        self.gammas = []
        self.neutrons = []

        # Flag to track if the timer event is set
        self.sprite_timer_set = False

        # Define orbit parameters
        self.orbit_center = (1920 // 2, 1080 // 2)  # Center of the screen
        self.orbit_radius = 400  # Radius of the orbit
        self.orbit_speed = 0.3  # Speed of orbit in degrees/frame
        
        # Spectroscopy minigame toggle
        self.spectroGame_bool = False

        # Magfield minigame toggle
        self.magfieldGame_bool = False

        # Set the display mode to fullscreen with the specified game resolution
        game_width, game_height = 1920, 1080
        self.screen = pygame.display.set_mode((game_width, game_height), pygame.FULLSCREEN)

        # Initialize time variables
        self.last_sprite_generation_time = pygame.time.get_ticks()
        self.sprite_generation_interval = 1000  # Generate sprites every 1000 milliseconds (1 second)


    def update(self):
        # Update model state based on user input or other factors
        self.psyche_spacecraft.update_orbit(self.orbit_center, self.orbit_radius, self.orbit_speed)

        # Spectroscopy Game
        if self.spectroGame_bool:
            self.generate_sprites()
            self.spectroGame()
            if self.captures >= 10:
                self.spectroGame_bool = False
                self.captures = 0

    def generate_sprites(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_sprite_generation_time >= self.sprite_generation_interval:
            # Reset the timer
            self.last_sprite_generation_time = current_time
            
            # Randomly choose whether to spawn a gamma or neutron sprite
            if random.choice([True, False]):
                # Generate gamma sprite in the center of the screen
                self.gammas.append(GammaRay(960, 540))
            else:
                # Generate neutron sprite in the center of the screen
                self.neutrons.append(Neutrons(960, 540))

    def handle_collisions(self):
        # Handle GammaRay collisions
        for gamma in self.gammas[:]:  # Iterate over a copy of the list
            if self.psyche_spacecraft.check_collision(gamma):
                self.gammas.remove(gamma)  # Remove the collided gamma
                self.captures += 1
                print(self.captures)
                # Increment captured_gammas or handle as needed

        # Handle Neutron collisions
        for neutron in self.neutrons[:]:  # Iterate over a copy of the list
            if self.psyche_spacecraft.check_collision(neutron):
                self.neutrons.remove(neutron)  # Remove the collided neutron
                self.captures += 1
                print(self.captures)
                # Increment captured_neutrons or handle as needed

    def spectroGame(self):
        # Draw sprites onto the screen
        for gamma in self.gammas:
            self.screen.blit(gamma.image, gamma.rect)
        for neutron in self.neutrons:
            self.screen.blit(neutron.image, neutron.rect)

        # Update positions for gamma and neutron sprites
        for gamma in self.gammas:
            gamma.update_position(960, 540, 1920, 1080)
        for neutron in self.neutrons:
            neutron.update_position(960, 540, 1920, 1080)
