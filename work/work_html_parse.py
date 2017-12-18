#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2017/12/18 0018.
# @Link    : http://blog.csdn.net/lftaoyuan
# Github   : https://github.com/seeways
# @Remark  : Python学习群：315857408
# 找一个网页，例如https://www.python.org/events/python-events/，用浏览器查看源码并复制
# 尝试解析一下HTML，输出Python官网发布的会议时间、名称和地点。
from urllib import request
from bs4 import BeautifulSoup

url = "https://www.python.org/events/python-events/"


def crawl_page(path):
    return request.urlopen(url).read().decode("utf-8")


def parse_web(data):
    soup = BeautifulSoup(data, "html.parser")
    conference_list = soup.find('ul', attrs={'class': 'list-recent-events menu'})
    for li in conference_list.find_all("li"):
        print("meeting name:", li.find('h3', attrs={'class': 'event-title'}).getText())  # 名称
        print("time:", li.find('time').getText())
        print("address:", li.find('span', attrs={"class": "event-location"}).getText()+"\n")


if __name__ == '__main__':
    # print(crawl_page(url))
    parse_web(crawl_page(url))

"""
结果
meeting name: PyCascades 2018
time: 22 Jan. – 24 Jan.  2018
address: Granville Island Stage, 1585 Johnston St, Vancouver, BC V6H 3R9, Canada

meeting name: PyCon Cameroon 2018
time: 24 Jan. – 29 Jan.  2018
address: Limbe, Cameroon

meeting name: FOSDEM 2018
time: 03 Feb. – 05 Feb.  2018
address: ULB Campus du Solbosch, Av. F. D. Roosevelt 50, 1050 Bruxelles, Belgium

meeting name: PyCon Pune 2018
time: 08 Feb. – 12 Feb.  2018
address: Pune, India

meeting name: PyCon Colombia 2018
time: 09 Feb. – 12 Feb.  2018
address: Medellin, Colombia

meeting name: PyTennessee 2018
time: 10 Feb. – 12 Feb.  2018
address: Nashville, TN, USA
"""