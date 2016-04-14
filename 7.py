import re
import os
import socket
import sys
import urllib.request
import http.cookiejar
import time
url='http://www.douban.com'

targetPath='E:\PathWorkPlaceLoad'
def saveFile(data):
    try:
        p=os.path.join(targetPath,("web.txt"))
        fo=open(p,'wb+')
        fo.write(data)
        fo.close()
    except:
        print("file creat fail...")
def destPath(path):
    if not os.path.isdir(targetPath):
        os.mkdir(targetPath)
    pos=path.rindex("/")   #http://img3.douban.com/icon/g273410-4.jpg   最后一个‘/’
    t=os.path.join(targetPath,path[pos+1:])
    return t                #返回一个完整路径
def myOpener(head = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
}):
    cj=http.cookiejar.CookieJar()
    pro=urllib.request.HTTPCookieProcessor(cj)
    opener=urllib.request.build_opener(pro)
    header=[]
    for key,value in head.items():
        elem=(key,value)
        header.append(elem)
    opener.addheaders=header
    return opener

opener=myOpener()
data=opener.open(url)
msg=data.info()
rurl=data.geturl()
data=data.read()
saveFile(data)
for link,s in set(re.findall(r'(http:[^s]*?(jpg|png|gif))', str(data))):  #正则表达式查找所有的图片
        print(link)
        try:
           urllib.request.urlretrieve(link, destPath(link))
        except:
            print("download fail...")

