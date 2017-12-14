#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/8 0008.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408

background_image_filename = 'C:\\Users\\Administrator\\Desktop\\image.png'
mouse_image_filename = 'C:\\Users\\Administrator\\Desktop\\123.png'
# 指定图像文件名称

import pygame
# 导入pygame库
from pygame.locals import *
# 导入一些常用的函数和常量
from sys import exit

# 向sys模块借一个exit函数用来退出程序

pygame.init()
# 初始化pygame,为使用硬件做准备

screen = pygame.display.set_mode((640, 480), 0, 32)
# 创建了一个窗口
pygame.display.set_caption("Hello, World!")
# 设置窗口标题

background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()
# 加载并转换图像

while True:
    # 游戏主循环

    for event in pygame.event.get():
        if event.type == QUIT:
            # 接收到退出事件后退出程序
            exit()

    screen.blit(background, (0, 0))
    # 将背景图画上去

    x, y = pygame.mouse.get_pos()
    # 获得鼠标位置
    x -= mouse_cursor.get_width() / 2
    y -= mouse_cursor.get_height() / 2
    # 计算光标的左上角位置
    screen.blit(mouse_cursor, (x, y))
    # 把光标画上去

    pygame.display.update()
    # 刷新一下画面
