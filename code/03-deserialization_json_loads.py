# -*- coding: utf-8 -*-
"""
------------------------------
# @Date     :2021/9/14 13:16
# @Author   :epover
# @Email    :endliss@sina.cn
------------------------------
"""
'''
    εεΊεε,json.loads
'''

import json

fp = open('names.txt','r')
result = json.loads(fp.read())
print(result)
print(type(result))
fp.close()