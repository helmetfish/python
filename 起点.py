import urllib.request
import re
import http.cookiejar
import time
import os
from bs4 import BeautifulSoup
targetPath='E:\小说'
url='http://read.qidian.com/BookReader/a4NTtnTCWIY1.aspx'

def makeDir(path):
    if not os.path.isdir(targetPath):
        t=os.mkdir(targetPath)
    pos=path.rindex('/')
    new_path=os.path.join(targetPath,path[pos+1:])
    return new_path
def myOpener(
    head= {
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
def downloading(num,block,huge):
    per=100*num*block/huge
    if per>100:
        per=100
    print("d---%.2f"%per)
    return per
def save_txt(data):
    try:
        fo=open(targetPath,'wb',name+'.txt')
        fo.write(data)
        fo.close
    except:
        print("creat fail...")

opener=myOpener()
op=opener.open(url)
soup=BeautifulSoup(op,'html.parser')
tag=soup.find_all('div',class_='download')
for t in tag:
    jokes=t.find('a')
    link=jokes.get('href')
    print(link)
try:
    time.sleep(2)
    print(link)
    urllib.request.urlretrieve(link,makeDir(link),downloading)
except:
    print("download fail")
    
