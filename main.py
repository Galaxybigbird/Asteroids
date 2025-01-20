import pygame
import random
from constants import *
from player import Player
from circleshape import Shot
from asteroidfield import Asteroid, AsteroidField

# Test if pygame is working
pygame.init()
print("PyGame version:", pygame.version.ver)

# Write main function that prints "Starting asteroids!"
def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Create game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Create clock object and dt variable
    clock = pygame.time.Clock()
    dt = 0
    
    # Create sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # Set up containers for Player, Asteroid, and Shot classes
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    
    # Create player in the middle of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    # Create asteroid field and add to updatable group
    asteroid_field = AsteroidField()
    updatable.add(asteroid_field)
    
    # Game loop
    while True:
        # Handle events (window closing)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Fill screen with black
        screen.fill((0, 0, 0))
        
        # Update all sprites
        for sprite in updatable:
            sprite.update(dt)
        
        # Check for collisions between player and asteroids
        for asteroid in asteroids:
            if player.collides(asteroid):
                print("Game Over!")
                return
                
        # Check for collisions between shots and asteroids
        for shot in shots:
            for asteroid in asteroids:
                if shot.collides(asteroid):
                    # Remove the shot and split the asteroid
                    shot.kill()
                    asteroid.split()
                    break  # Shot is destroyed, move to next shot
        
        # Draw all sprites
        for sprite in drawable:
            sprite.draw(screen)
        
        # Update display
        pygame.display.flip()
        
        # Control FPS and get delta time
        dt = clock.tick(60) / 1000.0  # Convert milliseconds to seconds

# Add if __name__ == "__main__" statement
if __name__ == "__main__":
    main()




