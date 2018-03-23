#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2018/3/23 0023. 
# @Link    : http://blog.csdn.net/lftaoyuan  
# Github   : https://github.com/seeways

# 按关键词爬取头条的图片(因为头条比较友好)


import os
import requests

# 默认地址本文件同级目录下新建img，可参考base_demo包的test28_path模块进行修改
save_path = os.path.abspath(os.path.join(os.getcwd(), "img"))


# 关键词
kw = ''

if not os.path.exists(save_path):
    os.mkdir(save_path)

while True:

    kw = input('请输入关键字:')

    # 范围个数
    for x in range(0, 100, 20):
        url = 'https://www.toutiao.com/search_content/?offset=' + str(x)\
              + '&format=json&keyword=%s&autoload=true&count=20&cur_tab=3&from=gallery' % kw
        response = requests.get(url)
        data = response.json()['data']
        if not data:
            print('down！')
            break

        for atlas in data:
            # 创建目录
            title = atlas['title']
            if title not in save_path:  # 防止文件名已经存在
                os.mkdir(os.path.join(save_path, title))
            k = 1  # 记录下载的图片数
            path = os.path.join(save_path, title)
            # 转进图片目录
            os.chdir(path)
            for image in atlas['image_list']:
                image_url = image['url'].replace('list', 'large')  # 改个链接获取大的图片
                atlas = requests.get('http:' + image_url).content
                with open(str(k) + '.jpg', 'wb') as f:  # 把图片写入文件内
                    f.write(atlas)
                k += 1
            # 转出图片目录
            os.chdir(save_path)
