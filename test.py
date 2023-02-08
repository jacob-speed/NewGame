import pygame


# Create window
pygame.init()
window = pygame.display.set_mode((111, 111))
pygame.display.set_caption("Pygame Ball Game")
# Handle events
for event in pygame.event.get():
    print(event.type)
