import pygame
import sys
import random
import time


class magField1:
    def __init__(self):
        self.mini_screen_width = 500  # Change these values for your desired size
        self.mini_screen_height = 500
        self.transparency_value = 255
        self.mini_screen = None
        self.show_mini_screen = True

    def create_mini_screen(self):
        self.mini_screen = pygame.Surface((self.mini_screen_width, self.mini_screen_height))
        self.mini_screen.set_alpha(self.transparency_value)
        # Draw elements on the mini-screen here
        if self.show_mini_screen:
            print("hi")
            # Define colors
            WHITE = (255, 255, 255)
            GRAY = (150, 150, 150)
            GREEN = (0, 255, 0)
            RED = (255, 0, 0)

            # Set the dimensions of the window
            WINDOW_SIZE = (1225, 800)
            screen = pygame.display.set_mode(WINDOW_SIZE)
            pygame.display.set_caption("Memory Game")

            # Set up the grid
            GRID_SIZE = 3
            SQUARE_SIZE = min(WINDOW_SIZE[0] // GRID_SIZE, WINDOW_SIZE[1] // GRID_SIZE)

            # Generate a random pattern
            pattern = [[random.randint(0, 1) for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

            # Main loop
            running = True
            show_pattern = True
            user_pattern = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
            correct_guesses = 0  # Track the number of correct guesses

            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button clicked
                        if not show_pattern:
                            # Get the coordinates of the mouse click
                            x, y = pygame.mouse.get_pos()
                            # Convert the coordinates to grid indices
                            row = y // SQUARE_SIZE
                            col = x // SQUARE_SIZE
                            # Toggle the user's pattern
                            if row < GRID_SIZE and col < GRID_SIZE:
                                user_pattern[row][col] = 1 if user_pattern[row][col] == 0 else 0

                screen.fill((0, 0, 0))  # Fill with white background

                if show_pattern:
                    # Clear the screen before showing the pattern
                    pygame.display.flip()
                    time.sleep(1)  # Add a short delay before showing the pattern
                    # Show the pattern one by one
                    for row in range(GRID_SIZE):
                        for col in range(GRID_SIZE):
                            if pattern[row][col] == 1:
                                pygame.draw.rect(screen, WHITE, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                    pygame.display.flip()
                    time.sleep(1)  # Add a delay after showing the pattern
                    show_pattern = False
                else:
                    # Draw the grid for user input
                    for row in range(GRID_SIZE):
                        for col in range(GRID_SIZE):
                            color = GREEN if user_pattern[row][col] == 1 else GRAY
                            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

                    pygame.display.flip()

                    # Check if the user's pattern matches the generated one
                    if user_pattern == pattern:
                        print("Congratulations! You matched the pattern.")
                        correct_guesses += 1
                        if correct_guesses >= 3:  # Stop the game if 3 correct guesses are made
                            running = False
                        else:
                            # Generate a new random pattern
                            pattern = [[random.randint(0, 1) for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
                            show_pattern = True
                            user_pattern = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
                    elif sum(sum(row) for row in user_pattern) == sum(sum(row) for row in pattern):
                        print("Oops! Incorrect pattern. Try again.")
                        # Stop the game if the user guesses incorrectly
                        running = False

            pygame.quit()