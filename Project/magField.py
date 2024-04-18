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
        self.GRID_SIZE = 3
        self.SQUARE_SIZE = 200
        self.pattern = None

    def generate_pattern(self):
        # Define the desired number of boxes in the pattern
        desired_num_boxes = 3  # Change this to your desired number of boxes

        # Generate a random pattern with exactly 3 boxes
        self.pattern = [[0] * self.GRID_SIZE for _ in range(self.GRID_SIZE)]
        boxes_added = 0
        while boxes_added < desired_num_boxes:
            # Choose a random cell
            row = random.randint(0, self.GRID_SIZE - 1)
            col = random.randint(0, self.GRID_SIZE - 1)
            # If the cell is currently 0, set it to 1
            if self.pattern[row][col] == 0:
                self.pattern[row][col] = 1
                boxes_added += 1

    def create_mini_screen(self, main_screen):
        pygame.init()
        self.mini_screen = pygame.Surface((main_screen.get_width(), main_screen.get_height()), pygame.SRCALPHA)  # Create a surface with per-pixel alpha

        # Define colors
        WHITE = (255, 255, 255)
        GRAY = (150, 150, 150)
        GREEN = (0, 255, 0)
        RED = (255, 0, 0)

        self.generate_pattern()  # Generate the pattern
        
        # Main loop
        running = True
        show_pattern = True
        user_pattern = [[0] * self.GRID_SIZE for _ in range(self.GRID_SIZE)]
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
                        row = y // self.SQUARE_SIZE
                        col = x // self.SQUARE_SIZE
                        # Toggle the user's pattern
                        if row < self.GRID_SIZE and col < self.GRID_SIZE:
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
                for row in range(self.GRID_SIZE):
                    for col in range(self.GRID_SIZE):
                        pygame.draw.rect(self.mini_screen, GRAY, (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE, self.SQUARE_SIZE, self.SQUARE_SIZE))

                # Show the pattern one by one
                for row in range(self.GRID_SIZE):
                    for col in range(self.GRID_SIZE):
                        if self.pattern[row][col] == 1:
                            pygame.draw.rect(self.mini_screen, WHITE, (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE, self.SQUARE_SIZE, self.SQUARE_SIZE))
                
                main_screen.blit(self.mini_screen, (0, 0))  # Blit mini_screen onto main_screen
                pygame.display.flip()
                # Check if one second has elapsed
                if pygame.time.get_ticks() - start_time >= 3000:  # 1000 milliseconds = 1 second
                    show_pattern = False
                    start_time = pygame.time.get_ticks()  # Reset the start time
            else:
                # Draw the user's grid
                for row in range(self.GRID_SIZE):
                    for col in range(self.GRID_SIZE):
                        color = GREEN if user_pattern[row][col] == 1 else GRAY
                        pygame.draw.rect(self.mini_screen, color, (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE, self.SQUARE_SIZE, self.SQUARE_SIZE))

                main_screen.blit(self.mini_screen, ((main_screen.get_width() - self.mini_screen.get_width()) // 2, (main_screen.get_height() - self.mini_screen.get_height()) // 2))  # Render the mini_screen in the center of the main screen
                pygame.display.flip()

                # Check if the user's pattern matches the generated one
                if self.patterns_match(user_pattern, self.pattern):
                    self.correct_guesses += 1
                    correct_guesses_string = str(self.correct_guesses)
                    print("Correct Guess, " + correct_guesses_string)
                    if self.correct_guesses >= 4:  # Stop the game if 3 correct guesses are made
                        running = False
                        return True  # Player has won
                    else:
                        # Generate a new random pattern
                        self.generate_pattern()  # Generate the pattern
                        show_pattern = True
                        user_pattern = [[0] * self.GRID_SIZE for _ in range(self.GRID_SIZE)]
                elif sum(sum(row) for row in user_pattern) == sum(sum(row) for row in self.pattern):
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
