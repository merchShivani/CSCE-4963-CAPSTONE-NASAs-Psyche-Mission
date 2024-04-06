import pygame
import math


class PsycheSpacecraft(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((100, 100))  # Placeholder image
#        self.image = pygame.image.load("path_to_spacecraft_image.png").convert()
        self.image.fill((0, 0, 255))  # Fill with blue color for now
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
#        self.image = pygame.image.load("gamma_ray.png").conve.rt()
        self.image = pygame.Surface((100, 50))  # Placeholder image
        self.image.fill((255, 0, 0))  # Fill with red color for now
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocity = 0
        self.direction = 1
        self.horizontal_speed = 3

    def update_position(self, dx, dy, screen_width, screen_height):
        self.velocity += 3
        new_x = self.rect.x + dx
        new_y = self.rect.y + dy
        new_y += self.velocity
        new_x += self.horizontal_speed * self.direction

        # Check if the new position is within screen boundaries
        if 0 <= new_x <= screen_width - self.rect.width:
            self.rect.x = new_x
        if 0 <= new_y <= screen_height - self.rect.height:
            self.rect.y = new_y

    def check_collision(self, other_sprite):
        return pygame.sprite.collide_rect(self, other_sprite)
    
class Neutrons(pygame.sprite.Sprite):
    def __init__(self, x, y):
  #      self.image = pygame.image.load("neutron.png").convert()
        self.image = pygame.Surface((100, 50))  # Placeholder image
        self.image.fill((0, 0, 0))  # Fill with black color for now
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update_position(self, dx, dy, screen_width, screen_height):
        new_x = self.rect.x + dx
        new_y = self.rect.y + dy

        # Check if the new position is within screen boundaries
        if 0 <= new_x <= screen_width - self.rect.width:
            self.rect.x = new_x
        if 0 <= new_y <= screen_height - self.rect.height:
            self.rect.y = new_y

    def check_collision(self, other_sprite):
        return pygame.sprite.collide_rect(self, other_sprite)
    
