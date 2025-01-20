import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    # Class variable for sprite groups
    containers = ()
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        # Draw the asteroid as a white circle
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
        
    def update(self, dt):
        # Move in straight line based on velocity
        self.position += self.velocity * dt
        
    def split(self):
        # Always destroy this asteroid
        self.kill()
        
        # If this was a small asteroid, we're done
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
            
        # Generate random split angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50)
        
        # Create two new velocity vectors by rotating current velocity
        velocity1 = self.velocity.rotate(random_angle)
        velocity2 = self.velocity.rotate(-random_angle)
        
        # Calculate new radius for child asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        # Create two new smaller asteroids
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        
        # Set their velocities (1.2x faster than parent)
        asteroid1.velocity = velocity1 * 1.2
        asteroid2.velocity = velocity2 * 1.2

class AsteroidField(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.spawn_timer = 0.0
        
    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer >= ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0
            
            # Spawn a new asteroid at a random edge
            edge = random.choice([0, 1, 2, 3])
            speed = 100  # pixels per second
            
            if edge == 0:  # Top
                position = pygame.Vector2(random.uniform(0, SCREEN_WIDTH), -ASTEROID_MAX_RADIUS)
                velocity = pygame.Vector2(0, 1)
            elif edge == 1:  # Right
                position = pygame.Vector2(SCREEN_WIDTH + ASTEROID_MAX_RADIUS, random.uniform(0, SCREEN_HEIGHT))
                velocity = pygame.Vector2(-1, 0)
            elif edge == 2:  # Bottom
                position = pygame.Vector2(random.uniform(0, SCREEN_WIDTH), SCREEN_HEIGHT + ASTEROID_MAX_RADIUS)
                velocity = pygame.Vector2(0, -1)
            else:  # Left
                position = pygame.Vector2(-ASTEROID_MAX_RADIUS, random.uniform(0, SCREEN_HEIGHT))
                velocity = pygame.Vector2(1, 0)
            
            # Randomize the velocity direction slightly
            velocity = velocity.rotate(random.uniform(-30, 30))
            velocity *= speed
            
            # Create asteroid with random size
            kind = random.randint(1, ASTEROID_KINDS)
            radius = ASTEROID_MIN_RADIUS * kind
            
            # Create and spawn the asteroid
            asteroid = Asteroid(position.x, position.y, radius)
            asteroid.velocity = velocity 