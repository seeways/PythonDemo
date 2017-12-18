#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/18 0018.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

"""
PIL：Python Imaging Library，Python平台事实上的图像处理标准库。
https://pillow.readthedocs.io
现在主要是志愿者在维护
"""


# # 图像缩放
# # 打开图片 os.path.abspath(os.path.join(os.getcwd(), "../img/logo.png"))
# img = Image.open("../img/logo.png")
# # 获得图像尺寸:
# w, h = img.size
# print('Original image size: %sx%s' % (w, h))
# # 缩放到50%:
# img.thumbnail((w // 2, h // 2))
# print('Resize image to: %sx%s' % (w // 2, h // 2))
# # 把缩放后的图像用jpeg格式保存:
# img.save('../img/logo_thumbnail.png', 'png')


# # 其他功能如切片、旋转、滤镜、输出文字、调色板等一应俱全。
# # 模糊效果
# img2 = img.filter(ImageFilter.BLUR)
# img2.save("../img/logo_thumbnail_blur.png", "png")


# PIL的ImageDraw提供了一系列绘图方法，让我们可以直接绘图。比如要生成字母验证码图片
def random_char():  # 字母
    return chr(random.randint(65, 90))


def random_color():  # 颜色
    return random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)


def random_color2():
    return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)


width = 60 * 4
height = 60
image = Image.new("RGB", (width, height), (255, 255, 255))
font = ImageFont.truetype("C:\Windows\Fonts\Arial.ttf", 36)  # 创建font
draw = ImageDraw.Draw(image)  # 创建draw
for x in range(width):  # 填充像素
    for y in range(height):
        draw.point((x, y), fill=random_color())

for t in range(4):  # 写字
    draw.text((60 * t + 10, 10), random_char(), font=font, fill=random_color2())


image = image.filter(ImageFilter.BLUR)  # 模糊
image.save("code.png", "png")
