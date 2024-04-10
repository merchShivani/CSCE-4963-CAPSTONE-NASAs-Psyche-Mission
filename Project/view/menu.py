import pygame
import os
import sys
# Add parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import get_project_root

is_fullscreen = True

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

    scaling_ratio = 1.0

    WIDTH *= scaling_ratio
    HEIGHT *= scaling_ratio

    if is_fullscreen == True:
        scaling_ratio = 1.0
        # Resize button images
        button_width, button_height = (1300 * 0.65) * scaling_ratio, (250 * 0.65) * scaling_ratio
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
        asteroid_width = 600 * scaling_ratio
        asteroid_height = 533 * scaling_ratio 
        asteroid = pygame.transform.scale(asteroid, (asteroid_width, asteroid_height))

        title_width = 2500 // 1.75 * scaling_ratio
        title_height = 500 // 1.75 * scaling_ratio
        title = pygame.transform.scale(title, (title_width, title_height))
        # Calculate title position to center it on the screen
        title_x = (WIDTH - title_width) // 2
        title_y = (HEIGHT - title_height) // 8
    elif is_fullscreen == False:
        scaling_ratio = 0.5
        # Resize button images
        button_width, button_height = (1300 * 0.65) * scaling_ratio, (250 * 0.65) * scaling_ratio
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
        asteroid_width = 600 * scaling_ratio
        asteroid_height = 533 * scaling_ratio 
        asteroid = pygame.transform.scale(asteroid, (asteroid_width, asteroid_height))

        title_width = 2500 // 1.75 * scaling_ratio
        title_height = 500 // 1.75 * scaling_ratio
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
                        handle_button_action(button["action"], screen, WIDTH, HEIGHT, pygame, main)

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

def toggle_mute(is_muted):
    # This is just a placeholder.
    # Implement muting game sounds here.
    return not is_muted

def show_options(screen, WIDTH, HEIGHT, pygame, get_project_root):
    options_running = True
    is_fullscreen = True

    # Constants for button colors and text
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    
    # Load and prepare assets
    root = get_project_root()
    background = pygame.image.load(os.path.join(root, "project/assets/images/background.png"))
    asteroid = pygame.image.load(os.path.join(root, "project/assets/images/psyche_asteroid.png"))
    title = pygame.image.load(os.path.join(root, "project/assets/images/title.png"))
    
    # Resize images
    asteroid = pygame.transform.scale(asteroid, (600, 533))  # Adjust dimensions as necessary
    title = pygame.transform.scale(title, (1250, 286))  # Adjust dimensions as necessary
    
    # Fonts
    font = pygame.font.Font(None, 36)
    
    # Button properties
    button_width, button_height = 200, 50
    full_rect = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2 - 60, button_width, button_height)
    mute_rect = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2, button_width, button_height)

    # "Back" button properties
    back_button_rect = pygame.Rect(10, 10, 100, 50)
    
    # Define initial angle for the asteroid rotation
    angle = 0

    while options_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Check if Escape is pressed
                    return  # Exit the options menu, going back to the previous menu/screen
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button_rect.collidepoint(event.pos):
                    return  
                if full_rect.collidepoint(event.pos):
                    # Toggle fullscreen logic
                    if is_fullscreen:
                        screen = pygame.display.set_mode((WIDTH / 2, HEIGHT / 2))
                        asteroid = pygame.transform.scale(asteroid, (300, 267))  # Adjust dimensions as necessary
                        title = pygame.transform.scale(title, (625, 143))  # Adjust dimensions as necessary
                        is_fullscreen = False
                    else:
                        screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
                        asteroid = pygame.transform.scale(asteroid, (600, 533))  # Adjust dimensions as necessary
                        title = pygame.transform.scale(title, (1250, 286))  # Adjust dimensions as necessary
                        is_fullscreen = True
                    # Adjust WIDTH and HEIGHT if necessary to match the new mode
                    WIDTH, HEIGHT = screen.get_size()
                    # After toggling, recalculate positions and sizes if necessary
                    full_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 60, 200, 50)
                    mute_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2, 200, 50)

                elif mute_rect.collidepoint(event.pos):
                    # Placeholder for mute toggle functionality
                    print("Mute toggle placeholder")

        screen.fill(BLACK)  # Draw background
        screen.blit(background, (0, 0))  # Place background image
        
        # Rotate and draw asteroid
        rotated_asteroid = pygame.transform.rotate(asteroid, angle)
        asteroid_rect = rotated_asteroid.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        screen.blit(rotated_asteroid, asteroid_rect.topleft)
        if is_fullscreen == True:
            angle += .8  # Increment the rotation angle for the next frame
        elif is_fullscreen == False:
            angle += .2

        # Draw the title
        screen.blit(title, ((WIDTH - title.get_width()) / 2, HEIGHT / 8))
        
        # Draw fullscreen and mute buttons
        pygame.draw.rect(screen, BLACK, full_rect)
        fs_text = font.render('Fullscreen', True, WHITE)
        screen.blit(fs_text, (full_rect.x + (button_width - fs_text.get_width()) / 2, full_rect.y + (button_height - fs_text.get_height()) / 2))
        
        pygame.draw.rect(screen, BLACK, mute_rect)
        mute_text = font.render('Mute', True, WHITE)
        screen.blit(mute_text, (mute_rect.x + (button_width - mute_text.get_width()) / 2, mute_rect.y + (button_height - mute_text.get_height()) / 2))

        # Draw "Back" button
        pygame.draw.rect(screen, BLACK, back_button_rect)  # "Back" button background
        back_text = font.render('Back', True, WHITE)
        screen.blit(back_text, (back_button_rect.x + (back_button_rect.width - back_text.get_width()) / 2, back_button_rect.y + (back_button_rect.height - back_text.get_height()) / 2))
        
        pygame.display.flip()


def handle_button_action(action, screen, WIDTH, HEIGHT, pygame, main):
    if action == "start_game":
        print("Starting the game!")
        main()
    elif action == "show_options":
        print("Opening options!")
        show_options(screen, WIDTH, HEIGHT, pygame, get_project_root)  # Pass the necessary arguments
    elif action == "quit_game":
        pygame.quit()
        sys.exit()

def is_a_pressed():
    keys = pygame.key.get_pressed()
    return keys[pygame.K_a]
