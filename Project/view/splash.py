import os
from utils import get_project_root

def splash(screen, WIDTH, HEIGHT, pygame):
    # No need to call pygame.init() here

    root = get_project_root()

    # Load the image
    splash_image = pygame.image.load(os.path.join(root, "project/assets/images/splash.png"))

    # Calculate scaled dimensions while preserving aspect ratio
    original_width, original_height = splash_image.get_size()
    aspect_ratio = original_width / original_height

    # Determine the maximum scaled dimensions with padding
    max_scaled_width = WIDTH - 100  # Adjust the padding as needed
    max_scaled_height = HEIGHT - 100  # Adjust the padding as needed

    if aspect_ratio > (max_scaled_width / max_scaled_height):
        # Fit width to maximum scaled width
        scaled_width = max_scaled_width
        scaled_height = int(scaled_width / aspect_ratio)
    else:
        # Fit height to maximum scaled height
        scaled_height = max_scaled_height
        scaled_width = int(scaled_height * aspect_ratio)

    # Scale the image
    splash_image = pygame.transform.scale(splash_image, (scaled_width, scaled_height))

    # Center the image on the screen
    offset_x = (WIDTH - scaled_width) // 2
    offset_y = (HEIGHT - scaled_height) // 2

    # Blit the scaled image onto the screen
    screen.blit(splash_image, (offset_x, offset_y))

    # Update the display
    pygame.display.flip()

    # Wait for a moment
    pygame.time.delay(3000)  # Adjust the delay time as needed
