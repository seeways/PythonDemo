#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2018/1/23 0023. 
# @Link    : http://blog.csdn.net/lftaoyuan  
# Github   : https://github.com/seeways
"""
来自django框架，实测可用，需要配置
"""
import os
from django.core.mail import send_mail, EmailMultiAlternatives


os.environ['DJANGO_SETTINGS_MODULE'] = 'MyBlog.settings'


if __name__ == '__main__':

    subject = "来自TaoYuan的测试邮件"
    from_email = "xxx@163.com"
    to = ["xxx@qq.com"]
    text_content = "Github: https://github.com/seeways    CSDN: http://blog.csdn.net/lftaoyuan"
    html_content = "<p>Github:<a href='https://github.com/seeways'>seeways</a></p><br><p>CSDN:<a " \
                   "href='http://blog.csdn.net/lftaoyuan'>TaoYuan</a></p> "

    # send_mail(主题， 内容， 发送者， 接收列表，其他默认参数)
    # send_mail(
    #     subject,
    #     text_content,
    #     from_email,
    #     to,
    #     html_message=html_content
    # )

    # EmailMultiAlternatives

    # 优先发送html_content, html内容无效时，发送text
    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()