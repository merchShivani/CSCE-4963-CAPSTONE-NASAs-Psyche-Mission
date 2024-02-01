import pygame


class GameView:
    def __init__(self):
        pygame.init()

        # Set your desired resolution
        game_width, game_height = 1920, 1080

        # Set the display mode to fullscreen with the specified game resolution
        self.screen = pygame.display.set_mode((game_width, game_height), pygame.FULLSCREEN)
        pygame.display.set_caption("Psyche")

        # Load multiple images from the "images" directory

        # Scale the images to the desired size

        # Get the rects of the images for positioning


        # Define positions for each image


    def update_display(self):
        # Clear the screen
        self.screen.fill((0, 0, 0))  # Fill with black background

        # Update the display
        pygame.display.flip()
