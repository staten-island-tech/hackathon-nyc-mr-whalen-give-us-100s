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
#rect= size of object, midbottom/midright=position of object
ratr_surface = pygame.image.load('playerrat_right.png').convert_alpha()
ratr_rect = ratr_surface.get_rect(midbottom = (40,400))
""" ratl_surface = pygame.image.load('playerrat_left.png').convert_alpha()
ratl_xpos = 1300 """
subway0_surface = pygame.image.load('subway0.png').convert_alpha() # convert to something pygame can work w, alpha = black n white backgrounds
subway0_rect = subway0_surface.get_rect(bottomright = (900,100))
subway1_surface = pygame.image.load('subway1.png').convert_alpha() # convert to something pygame can work w, alpha = black n white backgrounds
subway1_surface = pygame.transform.scale(subway1_surface, (int(subway1_surface.get_width() * 0.2), int(subway1_surface.get_height() * 0.2)))
subway1_rect = subway1_surface.get_rect(bottomright = (900,100))
subway2_surface = pygame.image.load('subway2.png').convert_alpha() # convert to something pygame can work w, alpha = black n white backgrounds
subway2_rect = subway2_surface.get_rect(bottomright = (1100,100))

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
        subway0_rect.x -= 2
        subway0_rect.y += 2
        if subway0_rect.bottom > 1100:
            subway0_rect.right = 900
            subway0_rect.bottom = 100
        screen.blit(subway0_surface, subway0_rect)

        # moving subway 1
        subway1_rect.x -= 1
        subway1_rect.y += 2
        if subway1_rect.bottom > 900:
            subway1_rect.right = 900
            subway1_rect.bottom = 100
        screen.blit(subway1_surface, subway1_rect)

        # moving subway 2
        subway2_rect.x += 2.6
        subway2_rect.y += 3
        if subway2_rect.bottom > 1100:
            subway2_rect.right = 1100
            subway2_rect.bottom = 100
        screen.blit(subway2_surface, subway2_rect)

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

        # collision w subway 0
        rat_mask = pygame.mask.from_surface(ratr_surface)
        subway0_mask = pygame.mask.from_surface(subway0_surface)
        offset0 = (subway0_rect.x - ratr_rect.x, subway0_rect.y - ratr_rect.y) 
        # the 3 lines above: the game ends only if the visible pixels of the images collide. idk why u write it this way tho lol i used chat gpt
        if rat_mask.overlap(subway0_mask, offset0):
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

        # collision w subway 1
        rat_mask = pygame.mask.from_surface(ratr_surface)
        subway1_mask = pygame.mask.from_surface(subway1_surface)
        offset1 = (subway1_rect.x - ratr_rect.x, subway1_rect.y - ratr_rect.y) 
        if rat_mask.overlap(subway1_mask, offset1):
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

        # collision w subway 2
        rat_mask = pygame.mask.from_surface(ratr_surface)
        subway2_mask = pygame.mask.from_surface(subway2_surface)
        offset2 = (subway2_rect.x - ratr_rect.x, subway2_rect.y - ratr_rect.y) 
        if rat_mask.overlap(subway2_mask, offset2):
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
        if ratr_rect.right > 1450:
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
            subway0_rect = subway0_surface.get_rect(bottomright = (900,100))
            subway1_rect = subway1_surface.get_rect(bottomright = (900,100))
            subway2_rect = subway2_surface.get_rect(bottomright = (1100,100))

    pygame.display.update()
    clock.tick(60)
