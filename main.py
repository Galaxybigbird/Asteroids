import pygame
from constants import *

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
    
    # Game loop
    while True:
        # Handle events (window closing)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Fill screen with black
        screen.fill((0, 0, 0))
        
        # Update display
        pygame.display.flip()

# Add if __name__ == "__main__" statement
if __name__ == "__main__":
    main()




