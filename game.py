import pygame

# Initialize Pygame
pygame.init()




# Set up the game window
:contentReference[oaicite:37]{index=37}
:contentReference[oaicite:38]{index=38}

# Define colors
:contentReference[oaicite:39]{index=39}

# Create the player sprite
:contentReference[oaicite:40]{index=40}
:contentReference[oaicite:41]{index=41}
:contentReference[oaicite:42]{index=42}
:contentReference[oaicite:43]{index=43}

# Set up the clock
:contentReference[oaicite:44]{index=44}

# Main game loop
running = True
while running:
    :contentReference[oaicite:45]{index=45}
        :contentReference[oaicite:46]{index=46}
            running = False

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player_rect.x += 5




# Set up the game window dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Crossy Road")

# Set up the game clock
clock = pygame.time.Clock()




#CREATING PLAYER CLASS
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))  # Red color
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

        # Keep the player within the screen boundaries
        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, SCREEN_HEIGHT - self.rect.height))


#creating cars class as the obstacles
class Car(pygame.sprite.Sprite):
    def __init__(self, y_position, speed):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))  # Green color
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = y_position
        self.speed = speed

    def update(self):
        self.rect.x -= self.speed
        if self.rect.x < -self.rect.width:
            self.rect.x = SCREEN_WIDTH

# Create sprite groups
def main():
    # Create sprite groups
    all_sprites = pygame.sprite.Group()
    cars = pygame.sprite.Group()

    # Create player instance
    player = Player()
    all_sprites.add(player)

    # Create car instances
    for i in range(5):
        car = Car(y_position=i * 100 + 100, speed=5)
        all_sprites.add(car)
        cars.add(car)

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update
        all_sprites.update()

        # Check for collisions
        if pygame.sprite.spritecollide(player, cars, False):
            print("Game Over!")
            running = False

        # Draw
        screen.fill((0, 0, 0))  # Black background
        all_sprites.draw(screen)

        # Update display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

    pygame.quit()






""" import turtle
from turtle import *
t = turtle.Turtle () """