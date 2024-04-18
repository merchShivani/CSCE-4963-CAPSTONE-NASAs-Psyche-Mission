import pygame
import random

class magField1:
    def __init__(self):
        self.mini_screen_width = 500  # Change these values for your desired size
        self.mini_screen_height = 500
        self.transparency_value = 255
        self.mini_screen = None
        self.show_mini_screen = True
        self.correct_guesses = 0  # Track the number of correct guesses

    def create_mini_screen(self, main_screen):
        pygame.init()
        self.mini_screen = pygame.Surface((main_screen.get_width(), main_screen.get_height()), pygame.SRCALPHA)  # Create a surface with per-pixel alpha

        # Draw elements on the mini-screen here
        if self.show_mini_screen:
            # Define colors
            WHITE = (255, 255, 255)
            GRAY = (150, 150, 150)
            GREEN = (0, 255, 0)
            RED = (255, 0, 0)

            # Set up the grid
            GRID_SIZE = 3
            SQUARE_SIZE = 200

            # Generate a random pattern
            pattern = [[random.randint(0, 1) for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

            # Main loop
            running = True
            show_pattern = True
            user_pattern = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
            start_time = pygame.time.get_ticks()  # Get the current time in milliseconds

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
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.quit_game()
                        if event.key == pygame.K_j:
                            self.model.magfieldGame_bool = False
                        pass
                    else:
                        # Pass other events back to the main event loop
                        pygame.event.post(event)

                # Clear the mini screen with a transparent background
                self.mini_screen.fill((255, 255, 255, 0))

                if show_pattern:
                    # Clear the mini screen with grey squares
                    for row in range(GRID_SIZE):
                        for col in range(GRID_SIZE):
                            pygame.draw.rect(self.mini_screen, GRAY, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

                    # Show the pattern one by one
                    for row in range(GRID_SIZE):
                        for col in range(GRID_SIZE):
                            if pattern[row][col] == 1:
                                pygame.draw.rect(self.mini_screen, WHITE, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                    
                    main_screen.blit(self.mini_screen, (0, 0))  # Blit mini_screen onto main_screen
                    pygame.display.flip()
                    # Check if one second has elapsed
                    if pygame.time.get_ticks() - start_time >= 3000:  # 1000 milliseconds = 1 second
                        show_pattern = False
                        start_time = pygame.time.get_ticks()  # Reset the start time
                else:
                    # Draw the user's grid
                    for row in range(GRID_SIZE):
                        for col in range(GRID_SIZE):
                            color = GREEN if user_pattern[row][col] == 1 else GRAY
                            pygame.draw.rect(self.mini_screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

                    main_screen.blit(self.mini_screen, ((main_screen.get_width() - self.mini_screen.get_width()) // 2, (main_screen.get_height() - self.mini_screen.get_height()) // 2))  # Render the mini_screen in the center of the main screen
                    pygame.display.flip()

                    # Check if the user's pattern matches the generated one
                    if self.patterns_match(user_pattern, pattern):
                        self.correct_guesses += 1
                        correct_guesses_string = str(self.correct_guesses)
                        print("Correct Guess, " + correct_guesses_string)
                        if self.correct_guesses >= 2:  # Stop the game if 3 correct guesses are made
                            running = False
                            return True  # Player has won
                        else:
                            # Generate a new random pattern
                            pattern = [[random.randint(0, 1) for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
                            show_pattern = True
                            user_pattern = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
                    elif sum(sum(row) for row in user_pattern) == sum(sum(row) for row in pattern):
                        print("Oops! Incorrect pattern. Try again.")
                        # Stop the game if the user guesses incorrectly
                        running = False

    def quit_game(self):
        pygame.quit()
        exit()
    
    # Define a function to check if two patterns match
    def patterns_match(self, pattern1, pattern2):
        for i in range(len(pattern1)):
            for j in range(len(pattern1[0])):
                if pattern1[i][j] != pattern2[i][j]:
                    return False
        return True

# Testing the magField1 class
if __name__ == "__main__":
    pygame.init()
    main_screen = pygame.display.set_mode((800, 600))
    game = magField1()
    game.create_mini_screen(main_screen)
