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
game_active = True

# background stuff
tracks_surface = pygame.image.load('subwaytracks2.jpg').convert() # no backgrounds, no need for alpha
text_surface = test_font.render('help the rat cross the subway tracks', True, 'White')
instructtext_surface = test_font.render('use WASD to move', True, 'White')

# moving stuff
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
        """ if event.type == pygame.KEYDOWN: # check if key is pressed
            if event.key == pygame.K_LSHIFT: # sprint but idk how to add cooldown
                ratr_rect.x += 20 """
        """ if event.type == pygame.KEYUP: # check if key is released
            print('stop moving up') """

    if game_active:
        # surface placement
        screen.blit(tracks_surface,(0,0))
        screen.blit(ratr_surface, ratr_rect)

        # moving subway 0
        subway_rect.x -= 2
        subway_rect.y += 2
        if subway_rect.bottom > 1100:
            subway_rect.right = 900
            subway_rect.bottom = 100
        screen.blit(subway_surface, subway_rect)

        screen.blit(text_surface,(100,50))
        screen.blit(instructtext_surface, (100,100))

        # rat controls
        keys = pygame.key.get_pressed() # this is a dictionary!
        if keys[pygame.K_w]: # look on official documentation for the specific names for keys
            ratr_rect.y -= 2
        if keys[pygame.K_s]:
            ratr_rect.y += 2
        if keys[pygame.K_d]:
            ratr_rect.x += 2
        if keys[pygame.K_a]:
            ratr_rect.x -= 2 

        # collision
        rat_mask = pygame.mask.from_surface(ratr_surface)
        subway_mask = pygame.mask.from_surface(subway_surface)
        offset = (subway_rect.x - ratr_rect.x, subway_rect.y - ratr_rect.y) 
        # the 3 lines above: the game ends only if the visible pixels of the images collide. idk why u write it this way tho lol i used chat gpt
        if rat_mask.overlap(subway_mask, offset):
            game_active = False
            screen.fill('goldenrod')
            deadratr_surface = pygame.image.load('playerrat_rdead.png')
            screen.blit(deadratr_surface,(50,200))
            endtext_surface = test_font.render('game over!!', True, 'White')
            screen.blit(endtext_surface,(950,200))
            hahatext_surface = test_font.render('u suck bro', True, 'White')
            screen.blit(hahatext_surface,(954,300))
            restarttext_surface = test_font.render('press r to restart', True, 'White')
            screen.blit(restarttext_surface,(900,400))

            """ keys = pygame.key.get_pressed() # this is a dictionary!
            if keys[pygame.K_r]:
                game_active = True
                ratr_rect = ratr_surface.get_rect(midbottom = (40,400))
                subway_rect = subway_surface.get_rect(bottomright = (900,100)) """
            """ pygame.quit()
            exit() """
        
        # completion
        if ratr_rect.right > 1600:
            game_active = False
            screen.fill('goldenrod')
            funnyrat_surface = pygame.image.load('veryroundrat.png')
            screen.blit(funnyrat_surface,(50,100))
            donetext_surface = test_font.render('you beat the game!!', True, 'White')
            screen.blit(donetext_surface,(850,200))
            restarttext_surface = test_font.render('press r to restart', True, 'White')
            screen.blit(restarttext_surface,(850,300))

            """ keys = pygame.key.get_pressed() # this is a dictionary!
            if keys[pygame.K_r]:
                game_active = True
                ratr_rect = ratr_surface.get_rect(midbottom = (40,400))
                subway_rect = subway_surface.get_rect(bottomright = (900,100)) """
            

    else:
        keys = pygame.key.get_pressed() # this is a dictionary!
        if keys[pygame.K_r]:
            game_active = True
            ratr_rect = ratr_surface.get_rect(midbottom = (40,400))
            subway_rect = subway_surface.get_rect(bottomright = (900,100))

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