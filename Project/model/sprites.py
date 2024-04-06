import pygame
import math


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.frames = []  # Add your animation frames here
        self.current_frame = 0
        self.image = pygame.Surface((50, 50))  # Placeholder image
        self.image.fill((255, 0, 0))  # Fill with red color for now
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def animate(self):
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        self.image = self.frames[self.current_frame]

    def check_collision(self, other_sprite):
        return pygame.sprite.collide_rect(self, other_sprite)

    def update_position(self, dx, dy, screen_width, screen_height):
        new_x = self.rect.x + dx
        new_y = self.rect.y + dy

        # Check if the new position is within screen boundaries
        if 0 <= new_x <= screen_width - self.rect.width:
            self.rect.x = new_x
        if 0 <= new_y <= screen_height - self.rect.height:
            self.rect.y = new_y

class PsycheSpacecraft(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((100, 100))  # Placeholder image
        self.image.fill((0, 0, 255))  # Fill with blue color for now
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.orbit_angle = 0   # Initial orbit angle
        self.major_axis = 750  # Major axis of the elliptical orbit
        self.minor_axis = 500  # Minor axis of the elliptical orbit

    def update_orbit(self, center, radius, speed):
        # Update spacecraft position based on orbit parameters
        self.orbit_angle += speed
        self.rect.centerx = center[0] + self.major_axis * math.cos(math.radians(self.orbit_angle))
        self.rect.centery = center[1] + self.minor_axis * math.sin(math.radians(self.orbit_angle))
        pass


