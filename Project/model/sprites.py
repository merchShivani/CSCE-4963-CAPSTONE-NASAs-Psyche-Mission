import random
import pygame
import math
import os
from utils import get_project_root


class PsycheSpacecraft(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        # Load the image of the spacecraft
        root = get_project_root()
        image_path = os.path.join(root, "project/assets/images/spacecraft.png")
        original_image = pygame.image.load(image_path).convert_alpha()

        # Resize the image
        self.image = pygame.transform.scale(original_image, (100, 100))

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.orbit_angle = 0   # Initial orbit angle
        self.major_axis = 250  # Major axis of the elliptical orbit
        self.minor_axis = 200  # Minor axis of the elliptical orbit
        self.move_out = False
        self.move_in = False

    def update_orbit(self, center, radius, speed):
        # Update spacecraft position based on orbit parameters
        self.orbit_angle += speed
        self.rect.centerx = center[0] + self.major_axis * math.cos(math.radians(self.orbit_angle))
        self.rect.centery = center[1] + self.minor_axis * math.sin(math.radians(self.orbit_angle))
        if self.move_out == True:
            self.major_axis = (self.major_axis + 1)
            self.minor_axis = (self.major_axis + 1)
        if self.move_in == True:
            self.major_axis = (self.major_axis - 1)
            self.minor_axis = (self.major_axis - 1)

        pass

    def check_collision(self, other_sprite):
        return pygame.sprite.collide_rect(self, other_sprite)

class GammaRay(pygame.sprite.Sprite):
    def __init__(self, x, y):
        root = get_project_root()
        self.image = pygame.image.load(os.path.join(root, "project/assets/images/gamma.png"))

        # Resize image
        w = 50  # Adjust the width as needed
        h = 50  # Adjust the height as needed
        self.image = pygame.transform.scale(self.image, (w, h))

        super().__init__()  # Initialize the sprite class

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocity = 0
        self.direction = 1
        self.horizontal_speed = 3
        self.speedx = random.randint(-5, 5)
        self.speedy = random.randint(-5, 5)

    def update_position(self, dx, dy, screen_width, screen_height):
        width, height = screen_width, screen_height
        new_x = self.rect.x + dx
        new_y = self.rect.y + dy

        # Define the margin distance from the edge
        margin = 20

        # Check if any part of the sprite is within the margin distance of the screen boundaries
        if (self.rect.right < margin or self.rect.left > width - margin or
            self.rect.bottom < margin or self.rect.top > height - margin):
            self.kill()  # Remove the sprite if it is within the margin distance of any screen boundary

        # Update the position of the sprite
        self.rect.x += self.speedx
        self.rect.y += self.speedy

    def check_collision(self, other_sprite):
        return pygame.sprite.collide_rect(self, other_sprite)

class Neutrons(pygame.sprite.Sprite):
    def __init__(self, x, y):
        root = get_project_root()
        self.image = pygame.image.load(os.path.join(root, "project/assets/images/neutron.png"))

        # Resize image
        w = 50  # Adjust the width as needed
        h = 50  # Adjust the height as needed
        self.image = pygame.transform.scale(self.image, (w, h))

        super().__init__()  # Initialize the sprite class

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocity = 0
        self.direction = 1
        self.horizontal_speed = 3
        self.speedx = random.randint(-5, 5)
        self.speedy = random.randint(-5, 5)

    def update_position(self, dx, dy, screen_width, screen_height):
        width, height = screen_width, screen_height
        new_x = self.rect.x + dx
        new_y = self.rect.y + dy

        # Define the margin distance from the edge
        margin = 20

        # Check if any part of the sprite is within the margin distance of the screen boundaries
        if (self.rect.right < margin or self.rect.left > width - margin or
            self.rect.bottom < margin or self.rect.top > height - margin):
            self.kill()  # Remove the sprite if it is within the margin distance of any screen boundary
            
        # Update the position of the sprite
        self.rect.x += self.speedx
        self.rect.y += self.speedy

    def check_collision(self, other_sprite):
        return pygame.sprite.collide_rect(self, other_sprite)