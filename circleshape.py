import pygame
from constants import SHOT_RADIUS

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # Call the parent class constructor
        if hasattr(self, 'containers'):
            super().__init__(self.containers)
        else:
            super().__init__()
            
        # Set position = pygame.Vector2(x, y)
        self.position = pygame.Vector2(x, y)
        # Set velocity = pygame.Vector2(0, 0)
        self.velocity = pygame.Vector2(0, 0)
        # Set radius = radius
        self.radius = radius

    def collides(self, other):
        # Calculate distance between centers
        distance = (self.position - other.position).length()
        # Return True if distance is less than or equal to sum of radii
        return distance <= (self.radius + other.radius)

    def draw(self, screen):
        # Sub-classes must override
        pass

    def update(self, dt):
        # Sub-classes must override
        pass

class Shot(CircleShape):
    # Class variable for sprite groups
    containers = ()
    
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        
    def draw(self, screen):
        # Draw the shot as a small white circle
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius)
        
    def update(self, dt):
        # Move in straight line based on velocity
        self.position += self.velocity * dt 