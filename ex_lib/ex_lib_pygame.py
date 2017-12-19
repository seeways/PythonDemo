#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/19 0019.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408
"""
https://www.pygame.org/docs/

WINDOWS:
anaconda lib
py -m pygame.examples.aliens

or run python in cmd
py -m pip install pygame --user
py -m pygame.examples.aliens


LINUX
LINUX 自带python2
Debian/Ubuntu/Mint
sudo apt-get install python3-pygame
python3 -m pygame.examples.aliens

Fedora/Red hat
sudo yum install python3-pygame
python3 -m pygame.examples.aliens
"""

import pygame
import sys

# https://www.pygame.org/docs/tut/PygameIntro.html
pygame.init()

size = width, height = 840, 480
speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.bmp")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
