import pygame
import time
import random
from pygame.locals import *
from pygame import mixer
pygame.init()
screen_loop = [(600,600),(580,600),(560,600),(540,600),(520,600),(500,600),(480,600),(460,600),(440,600),(420,600),(400,600),(380,600),(360,600),(340,600),(320,600),(300,600),(280,600),(260,600),(240,600),(220,600),(200,600),(180,600),(160,600),(140,600),(120,600),(100,600),(100,580),(100,560),(100,540),(100,520),(100,500),(100,480),(100,460),(100,440),(100,420),(100,400),(100,380),(100,360),(100,340),(100,320),(100,300),(100,280),(100,260),(100,240),(100,220),(100,200),(100,180),(100,160),(100,140),(100,120),(100,100),(120,100),(140,100),(160,100),(180,100),(200,100),(220,100),(240,100),(260,100),(280,100),(300,100),(320,100),(340,100),(360,100),(380,100),(400,100),(420,100),(440,100),(460,100),(480,100),(500,100),(520,100),(540,100),(560,100),(580,100),(600,100),(600,120),(600,140),(600,160),(600,180),(600,200),(600,220),(600,240),(600,260),(600,280),(600,300),(600,320),(600,340),(600,360),(600,380),(600,400),(600,420),(600,440),(600,460),(600,480),(600,500),(600,520),(600,540),(600,560),(600,580),(600,600)]
screen_width = 700
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
mixer.init()
mixer.music.load('simple-happy-acoustic-150094.mp3')
mixer.music.play()
num = 0
player_width = 35
player_height = 35
direction = 'left'
trail = [(400,400)]
apple = ((random.randint(70,600)),(random.randint(70,600)))
skin = (80, 157, 138)
score = 1
game_state = "start_menu"
def draw_start_menu(skin):
    screen.fill((42,28,14))
    pygame.draw.rect(screen, 'red',(500,200,50,50))
    pygame.draw.rect(screen, skin, (320,200,50,50))
    pygame.draw.rect(screen, skin, (270,200,50,50))
    pygame.draw.rect(screen, skin, (220,200,50,50))
    pygame.draw.rect(screen, skin, (220,235,50,50))
    pygame.draw.rect(screen, skin, (170,235,50,50))
    pygame.draw.rect(screen, skin, (170,270,50,50))
    pygame.draw.rect(screen, skin, (170,305,50,50))
    pygame.draw.rect(screen, skin, (170,305,50,50))
    fonttitle = pygame.font.SysFont('consolas', 60)
    font = pygame.font.SysFont('consolas', 35)
    title = fonttitle.render('SNAKE', True, (255, 255, 255))
    skin = font.render('S - Change Skin', True, (255, 255, 255))
    start_button = font.render('SPACE - Start', True, (255, 255, 255))
    screen.blit(title, (screen_width/2 - title.get_width()/2, screen_height/2.2 - title.get_height()/2))
    screen.blit(skin, (screen_width/2 - skin.get_width()/2, screen_height/1.8 + skin.get_height()/2))
    screen.blit(start_button, (screen_width/2 - start_button.get_width()/1.8, screen_height/1.6 + start_button.get_height()))
    pygame.display.update()

def draw_game_over_screen(score):
    screen.fill(((42,28,14)))
    fontTitle = pygame.font.SysFont('consolas', 60)
    font = pygame.font.SysFont('arial', 30)
    score = fontTitle.render('FINAL SCORE: ' + str(score), True, (255, 255, 255))
    title = fontTitle.render('GAME OVER', True, (255, 255, 255))
    restart_button = font.render('R - Restart', True, (255, 255, 255))
    quit_button = font.render('Q - Quit', True, (255, 255, 255))
    screen.blit(title, (screen_width/2 - title.get_width()/2, screen_height/4 - title.get_height()/2))
    screen.blit(score, (screen_width/2 - score.get_width()/2, screen_height/2.5 - score.get_height()/2))
    screen.blit(restart_button, (screen_width/2 - restart_button.get_width()/2, screen_height/1.9 + restart_button.get_height()))
    screen.blit(quit_button, (screen_width/2 - quit_button.get_width()/2, screen_height/2 + quit_button.get_height()/2))
    pygame.display.update()

def draw_skin_change():
    screen.fill((42,28,14)) 
    font = pygame.font.SysFont('consolas', 40)
    title = font.render('SKIN CHANGE', True, (255, 255, 255))
    color1 = font.render('Press 1', True, (247, 89, 205))
    color2 = font.render('Press 2', True, (96, 234, 158))
    color3 = font.render('Press 3', True, (246, 231, 155))
    color4 = font.render('Press 4', True, (127, 19, 67))
    ret = font.render('SPACE TO RETURN  ', True, (255, 255, 255))
    screen.blit(title, (screen_width/2 - title.get_width()/2, screen_height/5 - title.get_height()/2))
    screen.blit(color1, (screen_width/2 - color1.get_width()/2, (screen_height/3 - color1.get_height()/2)))
    screen.blit(color2, (screen_width/2 - color2.get_width()/2, (screen_height/3 - color2.get_height()/2)+100))
    screen.blit(color3, (screen_width/2 - color3.get_width()/2, (screen_height/3 - color3.get_height()/2)+200))
    screen.blit(color4, (screen_width/2 - color4.get_width()/2, (screen_height/3 - color4.get_height()/2)+300))
    screen.blit(ret, (screen_width/2 - ret.get_width()/2 +20, (screen_height/3 - ret.get_height()/2)+400))

def drawbox():
    font = pygame.font.SysFont('consolas', 20)
    title = font.render('Score: ' + str(score), True, (255, 255, 255))
    screen.blit(title, (500, 20))
    pygame.draw.line(screen, 'White', (50, 50), (650,50))
    pygame.draw.line(screen, 'White', (50, 50), (50,650))
    pygame.draw.line(screen, 'White', (650, 650), (650,50))
    pygame.draw.line(screen, 'White', (50, 650), (650,650))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    if pygame.mixer.music.get_busy() != True:
        mixer.music.load('simple-happy-acoustic-150094.mp3')
        mixer.music.play()
    if game_state == "start_menu":
        draw_start_menu(skin)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            player_x = trail[0][0]
            player_y = trail[0][1]
            game_state = "game"
            score = 1
            game_over = False

        if keys[pygame.K_s]:
            game_state = "skin_change"
    elif game_state == "game_over":
        trail.clear()
        trail.append((300,300))
        apple = ((random.randint(70,600)),(random.randint(70,600)))
        draw_game_over_screen(score)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            game_state = "start_menu"
        if keys[pygame.K_q]:
            pygame.quit()
            quit()
    elif game_state == "skin_change":
        draw_skin_change()
        if num >= len(screen_loop):
            num = 0
        pygame.draw.rect(screen, skin, (screen_loop[num][0], screen_loop[num][1], player_width, player_height))
        for i in range(1,2):
            pygame.draw.rect(screen,skin,(screen_loop[num-i][0], screen_loop[num-i][1], player_width, player_height))
            num += 1
            time.sleep (120.0 / 1000.0)
            pygame.display.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            skin = (247, 89, 205)
        if keys[pygame.K_2]:
            skin = (96, 234, 158)
        if keys[pygame.K_3]:
            skin = (246, 231, 155)
        if keys[pygame.K_4]:
            skin = (127, 19, 67)
        if keys[pygame.K_SPACE]:
            game_state = "start_menu"
    elif game_state == "game":
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            direction = 'left'
        elif keys[pygame.K_RIGHT]:
            direction = 'right'
        elif keys[pygame.K_UP]:
            direction = 'up'
        elif keys[pygame.K_DOWN]:
            direction = 'down'

        if direction == 'left':
            player_x -= 20
        if direction == 'right':
            player_x += 20 
        if direction == 'up':
            player_y -= 20 
        if direction == 'down':
            player_y += 20
            
        if player_x < 50 or player_x > screen_width-70 or player_y < 50 or player_y > screen_height-70:
            game_over = True
            game_state = "game_over"
        if (player_x, player_y) in trail:
            game_over = True
            game_state = "game_over"

        if apple[0] >= player_x  and  apple[0] <= player_x + 55:
            if apple[1] >= player_y and apple[1] <= player_y + 55:
                trail.append(apple)
                apple = ((random.randint(70,600)),(random.randint(70,600)))
                score += 1


        screen.fill((42,28,14))
        drawbox()
        cur = [trail[0]]
        trail[0] = (player_x, player_y)
        for i in range(1, len(trail)):
            cur.append((trail[i][0],trail[i][1]))
            trail[i] = cur[i-1]
         
        for location in trail:
            pygame.draw.rect(screen,skin,(location[0], location[1], player_width, player_height))

        pygame.draw.rect(screen,'Red', (apple[0], apple[1], player_height, player_width))
        pygame.display.update()
        time.sleep (120.0 / 1000.0)
  
    elif game_over:
        game_state = "game_over"
        game_over = False