# -*- conding:utf-8-*-
from lxml import etree 
import requests
import os

# 1请求包图网拿到数据
response = requests.get("https://ibaotu.com/shipin/")
# 3抽取标题，视频连接
xml = etree.HTML(response.text)
title_list = xml.xpath('//span[@class="video-title"]/text()')
src_list = xml.xpath('//div[@class="video-play"]/video/@src')
# print(title_list,src_list)
for title,src in zip(title_list, src_list):
    # print(title,src)
    # 3下载视频
    response1 = requests.get("http:"+src)
    # 4保存视频
    path = r"C:\Users\ASUS\Desktop\成果\photo"
    if not os.path.exists(path):
        os.makedirs(path)
    fileName = os.chdir(path)
    print("正在下载"+title)
    with open(title+".mp4","wb") as f:
        f.write(response1.content)
# 解析源码