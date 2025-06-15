# setup
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1400,800))
pygame.display.set_caption('Crossy Rat')
new_icon = pygame.image.load("fatrat.webp")
pygame.display.set_icon(new_icon)
clock = pygame.time.Clock()
test_font = pygame.font.Font('PixelifySans-VariableFont_wght.ttf',50)

# background stuff
tracks_surface = pygame.image.load('subwaytracks2.jpg').convert() # no backgrounds, no need for alpha
text_surface = test_font.render('omg a rat', True, 'White')

# moving stuff
subway_surface = pygame.image.load('subway2.png')
ratr_surface = pygame.image.load('playerrat_right.png').convert_alpha()
ratr_rect = ratr_surface.get_rect(midbottom = (40,400))
""" ratl_surface = pygame.image.load('playerrat_left.png').convert_alpha()
ratl_xpos = 1300 """
subway_surface = pygame.image.load('subway3.png').convert_alpha() # convert to something pygame can work w, alpha = black n white backgrounds
subway_rect = subway_surface.get_rect(bottomright = (900,100))

# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # surface placement
    screen.blit(tracks_surface,(0,0))
    screen.blit(text_surface,(100,50))

    # moving rat
    """ ratr_xpos += 4
    if ratr_xpos > 1600:
        ratl_xpos -= 4
        screen.blit(ratl_surface,(ratl_xpos, rat_ypos))
    screen.blit(ratr_surface,(ratr_xpos,rat_ypos)) """

    # moving subway 3
    subway_rect.x -= 2
    subway_rect.y += 2
    if subway_rect.bottom > 1100:
        subway_rect.right = 900
        subway_rect.bottom = 100
    screen.blit(subway_surface, subway_rect)
    screen.blit(ratr_surface, ratr_rect)

    pygame.display.update()
    clock.tick(60)




""" SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
PLAYER_SPEED = 5
CAR_SPEED = 3
ROAD_SPEED = 2

PURPLE = (128, 0, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Crossy Road")

clock = pygame.time.Clock()
running = True



player = pygame.Rect(300, 220, 40, 40)  # x, y, width, height
obstacle = pygame.Rect(200, 200, 100, 100)  # x, y, width, height


#CREATING PLAYER CLASS
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)  # Red color
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)
        self.speed = PLAYER_SPEED

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # Keep the player within the screen boundaries
        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, SCREEN_HEIGHT - self.rect.height))


#creating cars class as the obstacles
class Car(pygame.sprite.Sprite):
    def __init__(self, y_position, speed):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)  # Green color
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = y_position
        self.speed = speed



class oad(pygame.sprite.Sprite):
    def __init__(self, y, speed):
        super().__init__()
        self.image = pygame.Surface((SCREEN_WIDTH, 100))
        self.image.fill((50, 50, 50))  # Dark gray road
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = y_position
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.y = -self.rect.height


def create_car_lanes():
    lanes = []
    for i in range(5):
        speed = random.choice([3, 4, 5])
        lane = pygame.sprite.Group()
        for j in range(3):
            car = Car(SCREEN_WIDTH, i * 100 + 100, speed)
            lane.add(car)
        lanes.append(lane)
    return lanes


def check_collisions(player, lanes):
    for lane in lanes:
        for car in lane:
            if player.rect.colliderect(car.rect):
                return True
    return False

# Create sprite groups
all_sprites = pygame.sprite.Group()
cars = pygame.sprite.Group()

# Create player instance
player = Player()
all_sprites.add(player)

# Create car instances
for i in range(5):
    car = Car(y_position=i * 100 + 100, speed=CAR_SPEED)
    all_sprites.add(car)
    cars.add(car)

for i in range(3):
    road = Road(y_position=i * 100 + 50, speed=ROAD_SPEED)
    all_sprites.add(road)
    roads.add(road)


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

if pygame.sprite.spritecollide(player, cars, False):
        print("YOU LOST...")
        running = False

screen.fill(PURPLE)
all_sprites.draw(screen)


    # Handle player movement
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:
        player.x -= player_speed
if keys[pygame.K_RIGHT]:
        player.x += player_speed
if keys[pygame.K_UP]:
        player.y -= player_speed
if keys[pygame.K_DOWN]:
        player.y += player_speed

if player.colliderect(obstacle):
        print("YOU LOST...")


pygame.display.flip()


# Set up the game clock
clock.tick(60)




pygame.quit() """