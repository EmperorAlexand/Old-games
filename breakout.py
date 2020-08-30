import pygame as pg
from random import *

pg.init()

display_width = 800
display_height = 600

gameDisplay = pg.display.set_mode((display_width,display_height))
pg.display.set_caption('Breakout')

clock = pg.time.Clock()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
purple = (255,0,255)
yellow = (255,255,0)
turqouise = (0,255,255)

colors = [red, green, blue, purple, yellow, turqouise]

bricks = []

xspawn = 20
yspawn = 40

padx = 300
pady = 500

ballx = 200
bally = 400

xTo = 5
yTo = 5

for i in range(6):
    for j in range(10):
        bricks.append([xspawn, yspawn, choice(colors)])
        xspawn += 77
    yspawn += 40
    xspawn = 20

while True:

    gameDisplay.fill(black)

    ballx += xTo
    bally += yTo

    brickpop = []

    for i in range(len(bricks)):
        pg.draw.rect(gameDisplay, bricks[i][2], (bricks[i][0], bricks[i][1], 60, 20))
        if bricks[i][1] == bally and bricks[i][0] - ballx < 60 and bricks[i][0] - ballx > 0:
            brickpop.append(bricks[i])
            yTo = -yTo

    for i in range(len(brickpop)):
        bricks.pop(bricks.index(brickpop[i]))

    if ballx >= 795 or ballx <= 0:
        xTo = -xTo
    if bally >= 595 or bally <= 0:
        yTo = -yTo
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            break
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                padx -= 50
            if event.key == pg.K_RIGHT:
                padx += 50

    if bally + yTo * 2 >= 500 and ballx < padx + 100 and ballx > padx:
        yTo = -yTo

    pg.draw.rect(gameDisplay, white, (ballx, bally, 10, 10))
    pg.draw.rect(gameDisplay, white, (padx, pady, 100, 20))

    clock.tick(30)
    pg.display.update()

quit()
