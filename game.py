import pygame

# Initialize Pygame
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
#rect= size of object, midbottom/midright=position of object
ratr_surface = pygame.image.load('playerrat_right.png').convert_alpha()
ratr_rect = ratr_surface.get_rect(midbottom = (40,400))
""" ratl_surface = pygame.image.load('playerrat_left.png').convert_alpha()
ratl_xpos = 1300 """
subway0_surface = pygame.image.load('subway0.png').convert_alpha() # convert to something pygame can work w, alpha = black n white backgrounds
subway0_rect = subway0_surface.get_rect(bottomright = (800,900))
subway1_surface = pygame.image.load('subway1.jpg').convert_alpha() # convert to something pygame can work w, alpha = black n white backgrounds
subway1_rect = subway1_surface.get_rect(bottomright = (900,1000))
subway2_surface = pygame.image.load('subway2.jpg').convert_alpha() # convert to something pygame can work w, alpha = black n white backgrounds
subway2_rect = subway2_surface.get_rect(bottomright = (1000,1100))

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

    # moving subway 0
    subway0_rect.x -= 2
    subway0_rect.y += 2
    if subway0_rect.bottom > 1100:
        subway0_rect.right = 900
        subway0_rect.bottom = 100
    screen.blit(subway0_surface, subway0_rect)
    screen.blit(ratr_surface, ratr_rect)

    # moving subway 1
    subway1_rect.x -= 0.508
    subway1_rect.y += 1.2
    if subway1_rect.bottom > 1200:
        subway1_rect.right = 1000
        subway1_rect.bottom = 200
    screen.blit(subway1_surface, subway1_rect)
    screen.blit(ratr_surface, ratr_rect)

    # moving subway 2
    subway2_rect.x -= 0.28
    subway2_rect.y += 1.3
    if subway2_rect.bottom > 1300:
        subway2_rect.right = 1055
        subway2_rect.bottom = 300
    screen.blit(subway2_surface, subway2_rect)
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

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Crossy Rat")
""" new_icon = pygame.image.load("fattie.webp")
pygame.display.set_icon(new_icon)
 """


clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



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



class Road(pygame.sprite.Sprite):
    def __init__(self, y_position, speed):
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
for i in range(3):
    road = Road(y_position=i * 100 + 50, speed=ROAD_SPEED)
    all_sprites.add(road)


class RoadIterable:
    def __init__(self, num_roads, y_offset=50, speed=ROAD_SPEED):
        self.num_roads = num_roads
        self.y_offset = y_offset
        self.speed = speed

    def __iter__(self):
        for i in range(self.num_roads):
            yield Road(y_position=i * 100 + self.y_offset, speed=self.speed)

roads = RoadIterable(3)
for road in roads:
    all_sprites.add(road)


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




pygame.display.flip()


# Set up the game clock
clock.tick(60)



pygame.quit()