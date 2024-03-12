import pygame
import sys

class Spectrometer:
    def __init__(self):
        # Initialize Pygame
        pygame.init()

        # Get the screen dimensions
        self.screen_width, self.screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
        self.current_screen = None


    def set_screen(self, caption):
        # Set up the screen and display caption
        self.current_screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.FULLSCREEN)
        pygame.display.set_caption(caption)

    def run(self):
        # Define colors
        white = (255, 255, 255)

        # Main game loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        # Create a new screen
                        self.set_screen("New Screen")
                        self.current_screen.fill(white)  # Fill the new screen with a white background

            pygame.display.flip()
        # Quit Pygame
        pygame.quit()
        sys.exit()
