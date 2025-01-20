import pygame
from circleshape import CircleShape, Shot
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOT_SPEED, PLAYER_SHOOT_COOLDOWN

class Player(CircleShape):
    # Class variable for sprite groups
    containers = ()
    
    def __init__(self, x, y):
        # Call parent constructor with PLAYER_RADIUS
        super().__init__(x, y, PLAYER_RADIUS)
        # Initialize rotation to 0
        self.rotation = 0
        # Initialize shoot timer
        self.shoot_timer = 0

    def shoot(self):
        # Only shoot if the timer is 0
        if self.shoot_timer <= 0:
            # Create a shot at the player's position
            shot = Shot(self.position.x, self.position.y)
            # Create a velocity vector pointing up (same direction as player triangle)
            shot.velocity = pygame.Vector2(0, 1)
            # Rotate it to match player's rotation
            shot.velocity = shot.velocity.rotate(self.rotation)
            # Scale to shot speed
            shot.velocity *= PLAYER_SHOT_SPEED
            # Reset the timer
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN
            return shot

    def move(self, dt):
        # Create a unit vector pointing up (0, 1)
        forward = pygame.Vector2(0, -1)
        # Rotate it by our current rotation
        forward = forward.rotate(self.rotation)
        # Scale by speed and dt
        forward *= PLAYER_SPEED * dt
        # Add to our position
        self.position += forward

    def triangle(self):
        # Calculate triangle points based on position and rotation
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90)
        
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius + right * self.radius / 1.5
        c = self.position - forward * self.radius - right * self.radius / 1.5
        
        return [a, b, c]

    def draw(self, screen):
        # Draw the player as a white triangle
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def update(self, dt):
        # Get keyboard state
        keys = pygame.key.get_pressed()
        
        # Handle rotation
        if keys[pygame.K_a]:  # Left
            self.rotation -= PLAYER_TURN_SPEED * dt
        if keys[pygame.K_d]:  # Right
            self.rotation += PLAYER_TURN_SPEED * dt
            
        # Handle movement
        if keys[pygame.K_w]:  # Forward
            self.move(dt)
        if keys[pygame.K_s]:  # Backward
            self.move(-dt)
            
        # Update shoot timer
        if self.shoot_timer > 0:
            self.shoot_timer -= dt
            
        # Handle shooting
        if keys[pygame.K_SPACE]:
            self.shoot() 