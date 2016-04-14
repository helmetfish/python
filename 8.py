import re
import urllib
import http.cookiejar
import time
import os
from bs4 import BeautifulSoup


r='<div class="cont f14" id="postmessage_[0-9]{8}">(.*)?</div>[\r\n\s]+?<div id="post_rate_div_[0-9]{8}"'

pattern=re.compile(r,re.S)
mypath='E:\漫画'
def destPath(path):
    if not os.path.isdir(mypath):
        os.mkdir(mypath)
    pos=path.rindex("/")
    t=os.path.join(mypath,path[pos+1:])
    return t
def save_p(data):
    try:
        new_path=os.path.join(mypath,("暴走.txt"))
        fo=open(new_path,'wb+')
        fo.write(data)
        fo.close()
    except:
        print("Creat File Failed...")
def myOpener(head={
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
    }):
    cj=http.cookiejar.CookieJar()
    op=urllib.request.HTTPCookieProcessor(cj)
    opener=urllib.request.build_opener(op)
    header=[]
    for key,value in head.items():
        elem=(key,value)
        header.append(elem)
    opener.addheaders=header
    return opener

def downloading(size,block,huge):
    per=100*size*block/huge
    if per>100:
        per=100
    print("downloading----%.2f---"%per)
    return per
def page_loop(page):
    url='http://baozoumanhua.com/all/hot/page/%s?sv=1389592099'%page
    opener=myOpener()
    data=opener.open(url)
    soup=BeautifulSoup(data,"html.parser")
    tag=soup.find_all("div",class_="img-wrap")
    for t in tag:
        jokes=t.find('img')
        link=jokes.get('src')
        print(link)
        print(destPath(link))
        try:
            time.sleep(2)
            urllib.request.urlretrieve(link,destPath(link),downloading)
        except:
            print("download fail...")
for page in range(31,40):
    page_loop(page)



