#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2018/1/16 0016. 
# @Link    : http://blog.csdn.net/lftaoyuan  
# Github   : https://github.com/seeways

"""
参考http://www.liujiangblog.com/course/django/95
本文只是记录Django中数据库常用字段类型

from django.db import models
class MyModel(models.Model):
    user_name = models.CharField(max_length=30)
    is_reg = models.BooleanField()
    user_age = model.IntegerField()
    ...
"""




# 常用


"""
布尔值类型。默认值是None。
在HTML表单中体现为CheckboxInput标签。
如果要接收null值，请使用NullBooleanField。
"""
BooleanField


"""
字符串类型
必须接收一个max_length参数，表示字符串长度不能超过该值
默认的表单标签是input text
"""
CharField


"""
日期类型 datetime.date实例
class DateField(auto_now=False, auto_now_add=False, **options)

auto_now:每当对象被保存时将字段设为当前日期，常用于保存最后修改时间。
auto_now_add：每当对象被创建时，设为当前日期，常用于保存创建日期(不可修改)。

如需具备修改属性，添加默认参数即可
pub_time = models.DateField(auto_now_add=True)

DateTimeField比DateField 多了时分秒，其他一样
TimeField  只负责时分秒，其他一样
"""
DateField
DateTimeField
TimeField


"""
固定精度的十进制小数。

max_digits：最大的位数，必须大于或等于小数点位数 。
decimal_places：小数点位数，精度。
max_digits包含decimal_places的位数，如999.99
max_digits确定总位数，decimal_places确定小数点后位数

models.DecimalField(..., max_digits=5, decimal_places=2)
"""
DecimalField


"""
上传文件类型
class FileField(upload_to=None, max_length=100, **options)
默认情况下，该字段在HTML中表现为一个ClearableFileInput标签
在数据库内，我们实际保存的是一个字符串类型，默认最大长度100，可以通过max_length参数自定义。
真实的文件是保存在服务器的文件系统内的。

upload_to用于设置上传地址的目录和文件名
# 文件被传至`MEDIA_ROOT/uploads`目录，MEDIA_ROOT由你在settings文件中设置
upload = models.FileField(upload_to='uploads/')
# 被传到`MEDIA_ROOT/uploads/2015/01/30`目录，增加了一个时间划分
upload = models.FileField(upload_to='uploads/%Y/%m/%d/')
# 增加回调
# user_directory_path这种回调函数，必须接收两个参数，然后返回一个Unix风格的路径字符串。
# 参数instace代表一个定义了FileField的模型的实例，说白了就是当前数据记录。
# filename是原本的文件名。
def user_directory_path(instance, filename):
    #文件上传到MEDIA_ROOT/user_<id>/<filename>目录中
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class MyModel(models.Model):
    upload = models.FileField(upload_to=user_directory_path)
"""
FileField


"""
图像类型
使用Django的ImageField需要提前安装pillow模块
pip install pillow
class ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, **options)[source]
用于保存图像文件的字段。其基本用法和特性与FileField一样，只不过多了两个属性height和width。
height_field参数：保存有图片高度信息的模型字段名。 
width_field参数：保存有图片宽度信息的模型字段名。

使用FileField或者ImageField字段的步骤：

1. 在settings文件中，配置MEDIA_ROOT，作为你上传文件在服务器中的基本路径（这些文件不会被储存在数据库中）
2. 再配置个MEDIA_URL，作为公用URL，指向上传文件的基本路径。请确保Web服务器的用户账号对该目录具有写的权限。
3. 添加FileField或者ImageField字段到你的模型中，定义好upload_to参数，文件最终会放在MEDIA_ROOT目录的“upload_to”子目录中。
4. 所有真正被保存在数据库中的，只是指向你上传文件路径的字符串而已。可以通过url属性，在Django的模板中方便的访问这些文件。
5. 假设你有一个ImageField字段，名叫mug_shot，那么在Django模板的HTML文件中，可以使用{{ object.mug_shot.url }}来获取该文件。
6. 其中的object用你具体的对象名称代替。
7. 可以通过name和size属性，获取文件的名称和大小信息。
"""
ImageField


"""
一个自动增加的整数类型字段。
通常你不需要自己编写它，Django会自动帮你添加字段

Exemple:
id = models.AutoField(primary_key=True)
这是一个自增字段，从1开始计数。
如需设置主键，则需设置primary_key=True。

Django在一个模型中只允许有一个自增字段
且必须为主键！
"""
AutoField


"""
整数类型
取值范围-2147483648到2147483647
"""
IntegerField


"""
浮点数类型
"""
FloatField


"""
大量文本内容，在HTML中表现为Textarea标签
可以不设置max_length，如果设置了，还不如用CharField
"""
TextField


"""
用于保存通用唯一识别码（Universally Unique Identifier）的字段。
在PostgreSQL数据库中保存为uuid类型，其它数据库中为char(32)。
很多公司用作自增主键， 是自增主键的最佳替代品
import uuid     # Python的内置模块
from django.db import models

class MyUUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
"""
UUIDField


# 验证类常用

"""
IP类型
class GenericIPAddressField(protocol='both', unpack_ipv4=False, **options)[source]
参数protocol默认值为‘both’，可选‘IPv4’或者‘IPv6’
"""
GenericIPAddressField


"""
邮箱类型，默认max_length最大长度254位
使用这个字段的好处是，可以使用DJango内置的EmailValidator进行邮箱地址合法性验证。
"""
EmailField


"""
一个用于保存URL地址的字符串类型
默认最大长度200。
"""
URLField


# 其他


"""
Django1.10~
64位整数类型自增字段，数字范围更大
从1到9223372036854775807
"""
BigAutoField


"""
64位整数字段（看清楚，非自增），类似IntegerField
-9223372036854775808 到9223372036854775807。
在Django的模板表单里体现为一个textinput标签。
"""
BigIntegerField


"""
二进制数据类型。
"""
BinaryField


"""
逗号分隔的整数类型，必须接收一个max_length参数

这个我觉得很好，常用于表示较大的金额数目

例如1,000,000元。前端省事不少
"""
CommaSeparatedIntegerField


"""
持续时间类型，存储一定期间的时间长度，类似Python中的timedelta。
常用于进行时间之间的加减运算
"""
DurationField


"""
保存文件路径信息类型
class FilePathField(path=None, match=None, recursive=False, max_length=100, **options)[source]

path：必选参数。表示一个系统绝对路径。
match:可选参数，一个正则表达式，用于过滤文件名。只匹配基本文件名，不匹配路径。
例如foo.*\.txt$，只匹配文件名foo23.txt，不匹配bar.txt与foo23.png。
recursive:可选参数，只能是True或者False。默认为False。决定是否包含子目录（是否递归）。
allow_files:可选参数，只能是True或者False。默认为True。决定是否应该将文件名包括在内。
allow_folders： 可选参数，只能是True或者False。默认为False。决定是否应该将目录名包括在内。
allow_files和allow_folders，必须有一个为True。
FilePathField(path="/home/images", match="foo.*", recursive=True)
"""
FilePathField


"""
类似布尔字段，只不过额外允许NULL作为选项之一。
"""
NullBooleanField


"""
正整数字段，包含0,最大2147483647。
"""
PositiveIntegerField


"""
较小的正整数字段，从0到32767。
"""
PositiveSmallIntegerField


"""
slug是一个新闻行业的术语。
一个slug就是一个简短标签
包含字母、数字、下划线或者连接线，通常用于URLs中。
可以设置max_length参数，默认为50。
"""
SlugField


"""
小整数，包含-32768到32767。
"""
SmallIntegerField