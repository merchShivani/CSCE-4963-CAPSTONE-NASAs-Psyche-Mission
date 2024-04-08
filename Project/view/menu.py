import pygame
import os
import sys
# Add parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import get_project_root

def menu(screen, WIDTH, HEIGHT, pygame, main):
    root = get_project_root()

    # Constants
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Fonts
    title_font = pygame.font.Font(None, 72)
    button_font = pygame.font.Font(None, 36)

    # Load button images
    start = pygame.image.load(os.path.join(root, "project/assets/images/start.png"))
    options = pygame.image.load(os.path.join(root, "project/assets/images/options.png"))
    quit = pygame.image.load(os.path.join(root, "project/assets/images/quit.png"))

    # Resize button images
    button_width, button_height = (1300 * 0.65), (250 * 0.65)
    start = pygame.transform.scale(start, (button_width, button_height))
    options = pygame.transform.scale(options, (button_width, button_height))
    quit = pygame.transform.scale(quit, (button_width, button_height))

    # Button properties
    button_y = HEIGHT // 2  # Center vertically

    # Calculate x position for centering buttons horizontally
    start_x = WIDTH // 2 - button_width // 2
    options_x = WIDTH // 2 - button_width // 2
    quit_x = WIDTH // 2 - button_width // 2

    # Create buttons with different colors
    buttons = [
        {"image": start, "action": "start_game", "rect": start.get_rect(center=(start_x + button_width // 2, button_y))},
        {"image": options, "action": "show_options", "rect": options.get_rect(center=(options_x + button_width // 2, button_y + button_height + 10))},
        {"image": quit, "action": "quit_game", "rect": quit.get_rect(center=(quit_x + button_width // 2, button_y + 2 * (button_height + 10)))}
    ]

    background = pygame.image.load(os.path.join(root, "project/assets/images/background.png"))
    asteroid = pygame.image.load(os.path.join(root, "project/assets/images/psyche_asteroid.png"))
    title = pygame.image.load(os.path.join(root, "project/assets/images/title.png"))

    # Resize images
    asteroid_width = 600
    asteroid_height = 533 
    asteroid = pygame.transform.scale(asteroid, (asteroid_width, asteroid_height))

    title_width = 2500 // 1.75
    title_height = 500 // 1.75
    title = pygame.transform.scale(title, (title_width, title_height))
    # Calculate title position to center it on the screen
    title_x = (WIDTH - title_width) // 2
    title_y = (HEIGHT - title_height) // 8

    # Define initial angle of rotation
    angle = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button["rect"].collidepoint(event.pos):
                        handle_button_action(button["action"], main)

        # Draw background
        screen.fill(BLACK)
        screen.blit(background, (0, 0))

        # Rotate and draw asteroid
        rotated_asteroid = pygame.transform.rotate(asteroid, angle)
        # Calculate the offset for the rotated image
        rotated_rect = rotated_asteroid.get_rect(center=(40 + asteroid_width / 2, 400 + asteroid_height / 2))
        screen.blit(rotated_asteroid, rotated_rect)

        # Increment rotation angle
        angle += 1  # Adjust rotation speed as needed

        # Draw title and buttons
        screen.blit(title, (title_x, title_y))
        for button in buttons:
            screen.blit(button["image"], button["rect"])

        pygame.display.flip()
        pygame.time.Clock().tick(30)

def handle_button_action(action, main):
    if action == "start_game":
        print("Starting the game!")
        main()
    elif action == "show_options":
        print("Opening options!")
        # Add your code to show options here
    elif action == "quit_game":
        pygame.quit()
        sys.exit()

def is_a_pressed():
    keys = pygame.key.get_pressed()
    return keys[pygame.K_a]
