import pygame
from random import *
from winsound import Beep

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Epic Game')

clock = pygame.time.Clock()

black = (0,0,0)
white = (255,255,255)

x = 400
y = 300

x_ = 3
y_ = 3

_x = 200

while True:
    x += x_
    y += y_

    x += uniform(0.01, 0.05)

    gameDisplay.fill(black)
    pygame.draw.rect(gameDisplay, white, (x, y, 10, 10))

    if x < 0:
        x_ = -x_
        Beep(200, 20)
    if x > 790:
        x_ = -x_
        Beep(200, 20)
    if y < 0:
        y_ = -y_
        Beep(200, 20)
    if y > 590:
        y_ = -y_
        Beep(200, 20)

    if y + 8 >= 500 and x < _x + 100 and x > _x:
        y_ = -y_
        Beep(400, 40)

    pygame.draw.rect(gameDisplay, white, (_x, 500, 100, 10))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

        pygame.draw.rect(gameDisplay, white, (_x, 500, 100, 10))
        
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                _x -= 50

            if event.key == pygame.K_RIGHT:
                _x += 50

        print(event)

    pygame.draw.rect(gameDisplay, white, (_x, 500, 100, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
