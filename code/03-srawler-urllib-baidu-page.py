# -*- coding: utf-8 -*-
"""
------------------------------
# @Date     :2021/9/14 20:34
# @Author   :epover
# @Email    :endliss@sina.cn
------------------------------
"""

'''
    通过urllib爬取百度首页
'''

import urllib.request

# 1、定义url
url = 'http://www.baidu.com'
# 2、通过代码模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)
# 3、读取数据，一个字节一个字节的读取  read()方法返回的是字节形式的二进制，需要转换成utf-8
content = response.read().decode('utf-8')
print(content)