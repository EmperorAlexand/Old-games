import pygame
from random import *
from winsound import Beep

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

length = 1

x = 400
y = 300

parts = [[400, 300]]
xTo = None
yTo = None

snake_dir = None

food_x = randint(0, 39) * 20
food_y = randint(0, 29) * 20

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
        
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                snake_dir = 'x-'

            if event.key == pygame.K_RIGHT:
                snake_dir = 'x+'

            if event.key == pygame.K_UP:
                snake_dir = 'y-'

            if event.key == pygame.K_DOWN:
                snake_dir = 'y+'

        print(event)

    xTo = 0
    yTo = 0

    if snake_dir == 'x-':
        xTo = -20
    if snake_dir == 'x+':
        xTo = 20
    if snake_dir == 'y-':
        yTo = -20
    if snake_dir == 'y+':
        yTo = 20

    if parts[-1][0] == food_x and parts[-1][1] == food_y:
        food_x = randint(0, 39) * 20
        food_y = randint(0, 29) * 20
        length += 1
        parts.insert(0, [])
        parts[0].insert(0, parts[1][0])
        parts[0].insert(1, parts[1][1])

    gameDisplay.fill(black)

    parts[-1] = [parts[-1][0] + xTo, parts[-1][1] + yTo]

    if length > 1:
        try:
            for i in range(len(parts)):
                parts[i] = [parts[i + 1][0], parts[i + 1][1]]
                pygame.draw.rect(gameDisplay, white, (parts[i][0], parts[i][1], 20, 20))
        except IndexError:
            pass
    else:
        pygame.draw.rect(gameDisplay, white, (parts[0][0], parts[0][1], 20, 20))
        

    pygame.draw.rect(gameDisplay, red, (food_x, food_y, 20, 20))

    pygame.display.update()
    clock.tick(10)

pygame.quit()
quit()
