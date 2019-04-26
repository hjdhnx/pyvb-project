#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# File  : ico.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2019/4/25
# 这段程序可将图标1.ico转换成icon.py文件里的base64数据
import base64
open_icon = open("logo.ico","rb")
b64str = base64.b64encode(open_icon.read())
open_icon.close()
write_data = "img = '%s'" % b64str
f = open("icon.py","w+")
f.write(write_data)
f.close()