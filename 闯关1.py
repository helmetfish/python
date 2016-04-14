import urllib.request
import http.cookiejar
import re
import time
import requests
import threading
from bs4 import BeautifulSoup
import urllib.parse
'''
url='http://www.heibanke.com/lesson/crawler_ex00/'
pattern="\d+"
count=0
mutex=threading.Lock()
class Mythread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        global count,mutex,url
        #time.sleep(1)
        if mutex.acquire():
            op=urllib.request.urlopen(url)
            soup=BeautifulSoup(op,"html.parser")
            tag=soup.find('h3').get_text()
            p=re.compile(pattern,flags=0)
            num=p.findall(tag)
            pos=url.rindex('/')
        
            count=count+1
            print(count)
            url=url[0:pos+1]+num[0]
            print(url)
        mutex.release()
if __name__=="__main__":
    mission1=Mythread()
    mission1.start()


#51103 地址
#-----------------------Mission 2--------------------------
'''
url1='http://www.heibanke.com/lesson/crawler_ex01/'

header={
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Accept-Encoding': 'gzip,deflate',
    'DNT': '1'
    }
for pwd in range(0,31):
    try:    
        payload={'username':'john','password':pwd}
        s=requests.Session()
        r=s.post(url1,data=payload,headers=header)
        soup=BeautifulSoup(r.text,"html.parser")
        tag=soup.find('h3')
        print(tag.text)
        print(pwd)
    except:
        print("what")

