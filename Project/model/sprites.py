import random
import pygame
import math
import os
from utils import get_project_root


class PsycheSpacecraft(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        # Create a surface and fill it with blue color
        self.image = pygame.Surface((100, 100))
        self.image.fill((0, 0, 255))  # Fill with blue color

        #Load the image of the spacecraft
        root = get_project_root()
        image_path = os.path.join(root, "project/assets/images/spacecraft.png")
        spacecraft_image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.Surface((100, 100))  # Placeholder image
       
        #Resize image
        self.image.blit(pygame.transform.scale(spacecraft_image, (100, 100)), (0, 0))
        
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

        self.rect = self.image.get_rect()
        self.rect.center = (960, 540)
        self.velocity = 0
        self.direction = 1
        self.horizontal_speed = 3
        self.speedx = random.randint(-5, 5)
        self.speedy = random.randint(-5, 5)

    def update_position(self, dx, dy, screen_width, screen_height):
        width, height = 1920, 1200
        new_x = self.rect.x + dx
        new_y = self.rect.y + dy

        if not 0 < self.rect.x < width:
            self.speedx *= -1 # reverse direction
        self.rect.x += self.speedx

        if not 0 < self.rect.y < height:
            self.speedy *= -1 # reverse direction
        self.rect.y += self.speedy

        # Check if the new position is within screen boundaries
        #if 0 <= new_x <= screen_width - self.rect.width:
            #self.rect.x = new_x
        #if 0 <= new_y <= screen_height - self.rect.height:
            #self.rect.y = new_y

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

        self.rect = self.image.get_rect()
        self.rect.center = (960, 540)
        self.velocity = 0
        self.direction = 1
        self.horizontal_speed = 3
        self.speedx = random.randint(-5, 5)
        self.speedy = random.randint(-5, 5)

    def update_position(self, dx, dy, screen_width, screen_height):
        width, height = 1920, 1200
        new_x = self.rect.x + dx
        new_y = self.rect.y + dy

        if not 0 < self.rect.x < width:
            self.speedx *= -1 # reverse direction
        self.rect.x += self.speedx

        if not 0 < self.rect.y < height:
            self.speedy *= -1 # reverse direction
        self.rect.y += self.speedy

    def check_collision(self, other_sprite):
        return pygame.sprite.collide_rect(self, other_sprite)
    
