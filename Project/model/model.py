import random
import pygame
import time
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

        #Magfield minigame toggle
        self.magfieldGame_bool = False

        game_width, game_height = 1920, 1080
        # Set the display mode to fullscreen with the specified game resolution
        self.screen = pygame.display.set_mode((game_width, game_height), pygame.FULLSCREEN)

    def update(self):
            # Update model state based on user input or other factors
            self.psyche_spacecraft.update_orbit(self.orbit_center, self.orbit_radius, self.orbit_speed)

            # Spectroscopy Game
            if self.spectroGame_bool == True:
                 self.spectroGame()
            if ((self.captured_gammas == 5) and (self.captured_neutrons == 5)):
                 self.spectroGame_bool = False
                 print("Captured all")
            
            if self.magfieldGame_bool == True:
                self.magfieldGame()
            


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
    
    def magfieldGame(self):
        # Constants
        GRID_SIZE = 3
        SQUARE_SIZE = 100
        WINDOW_SIZE = (GRID_SIZE * SQUARE_SIZE, GRID_SIZE * SQUARE_SIZE)
        WHITE = (255, 255, 255)
        GRAY = (150, 150, 150)
        GREEN = (0, 255, 0)
        RED = (255, 0, 0)
        BLACK = (0, 0, 0)
        PATTERN_LENGTH = 5  # Adjusted pattern length to 5
        font = pygame.font.Font(None, 80)

        # Functions
        def generate_pattern():
            pattern = [[0] * PATTERN_LENGTH for _ in range(GRID_SIZE)]
            white_count = 0
            while white_count < PATTERN_LENGTH:
                for row in range(GRID_SIZE):
                    for col in range(PATTERN_LENGTH):
                        if random.randint(0, 1) == 1 and white_count < PATTERN_LENGTH:
                            pattern[row][col] = 1
                            white_count += 1
            return pattern

        def draw_pattern(pattern):
            for row in range(GRID_SIZE):
                for col in range(PATTERN_LENGTH):
                    color = WHITE if pattern[row][col] == 1 else GRAY
                    pygame.draw.rect(self.screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

        def get_user_pattern():
            user_pattern = [[0] * PATTERN_LENGTH for _ in range(GRID_SIZE)]
            clicked_boxes = 0
            while clicked_boxes < PATTERN_LENGTH:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        x, y = pygame.mouse.get_pos()
                        row = y // SQUARE_SIZE
                        col = x // SQUARE_SIZE
                        if row < GRID_SIZE and col < PATTERN_LENGTH and user_pattern[row][col] == 0:
                            user_pattern[row][col] = 1
                            clicked_boxes += 1
                            draw_user_pattern(user_pattern)
                            pygame.display.flip()
            return user_pattern

        def draw_user_pattern(pattern):
            for row in range(GRID_SIZE):
                for col in range(PATTERN_LENGTH):
                    color = GREEN if pattern[row][col] == 1 else GRAY
                    pygame.draw.rect(self.screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        
        def show_popup(message, x, y):
            # Clear the screen
            self.screen.fill(WHITE)

            # Render the message
            text = font.render(message, True, BLACK)
            text_rect = text.get_rect(center=(x, y))

            # Draw the message on the screen
            self.screen.blit(text, text_rect)

            # Update the display
            pygame.display.flip()

            # Wait for a short period of time
            pygame.time.wait(2000)

        def main():
            clock = pygame.time.Clock()

            correct_guesses = 0
            while correct_guesses < 3:
                pattern = generate_pattern()
                draw_pattern(pattern)
                pygame.display.flip()
                time.sleep(1)
                
                user_pattern = get_user_pattern()
                if user_pattern == pattern:
                    print("Congratulations! You matched the pattern.")
                    correct_guesses += 1
                else:
                    print("Oops! Incorrect pattern. Try again.")

                # Generate a new pattern for the next round
                print("Generating a new pattern...")
                time.sleep(1)

            print("You've won the game!")
            show_popup("You've won the game!", 800, 500)
            self.magfieldGame_bool = False
        main()