#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2018/1/10 0010.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408


from urllib import request
import datetime
import re
import os.path

to_find_string = "https://bd.phncdn.com/videos/"
big_path = ""


def save_file(this_download_url, path):
    print("- - - - - - - - - -- - - - - - - - - - - - - - - - - ")
    time1 = datetime.datetime.now()
    print(str(time1)[:-7], end=' ')
    if os.path.isfile(path):
        file_size = os.path.getsize(path) / 1024 / 1024
        print("File " + path + " (" + str(file_size) + "Mb) already exists.")
        return
    else:
        print("Downloading " + path + "...")
        f = request.urlopen(this_download_url)
        data = f.read()
        with open(path, "wb") as code:
            code.write(data)
        time2 = datetime.datetime.now()
        print(str(time2)[:-7], end=' ')
        print(path + " Done.")
        use_time = time2 - time1
        print("Time used: " + str(use_time)[:-7] + ", ", end=' ')
        file_size = os.path.getsize(path) / 1024 / 1024
        print(
            "File size: " + str(file_size) + " MB, Speed: " + str(file_size / (use_time.total_seconds()))[:4] + "MB/s")


def download_the_av(url):
    req = request.Request(url)
    content = request.urlopen(req).read()
    while len(content) < 100:
        print("try again...")
        content = request.urlopen(req).read()
    print("All length:" + str(len(content)))

    title_begin = content.find("<title>")
    title_end = content.find("</title>")
    title = content[title_begin + 7:title_end - 14]
    title = title.replace('/', '_')
    title = filter(lambda x: x in "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ _-", title)

    quality = ['720', '480', '240']
    for i in quality:
        find_position = content.find("\"quality\":\"" + i + "\"")
        if find_position > 0:
            print("Quality: " + i + "P")
            break
    to_find = content[find_position:find_position + 4000]

    pattern = re.compile(r"\"videoUrl\":\"[^\"]*\"")
    match = pattern.search(to_find)
    if match:
        the_url = match.group()
        the_url = the_url[12:-1]  # the real url
        the_url = the_url.replace("\\/", "/")
        save_file(the_url, big_path + title + ".mp4")


# http://www.x-pornhub.net/view_video.php?viewkey=ph592ef8731630a
urls = ["https://www.p***hub.com/view_video.php?viewkey=ph592ef8731630a", ]
print(len(urls), end=' ')
print(" videos to download...")
count = 0

for url in urls:
    print(count)
    count += 1
    download_the_av(url)
print("All done")
