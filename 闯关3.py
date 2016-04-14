import requests
import urllib.parse
import traceback
from bs4 import BeautifulSoup
url='http://www.heibanke.com/lesson/crawler_ex02/'
murl='http://www.heibanke.com/accounts/login/?next=/lesson/crawler_ex02/'
header={
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.8, en-US; q=0.5, en; q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586',
    'Accept-Encoding': 'gzip,deflate',
    'DNT': '1'
    }
#mycookie=dict(csrftoken='CdfEM7ktVb69e1CEch9JE061GrizLbvx')
s=requests.Session()                                                     # '''保持整个连接属于一个链接，确保token不会刷新'''

print('------------------------------Mission 3(1)-------------------------------')
r=s.get(murl)
soup=BeautifulSoup(r.text,'html.parser')
flag=soup.find('input')['value'] 
print('当前token1:%s'%flag)
uuid={
    'username':'john',
    'password':'qjklw123',
    'csrfmiddlewaretoken':flag
    }
r=s.post(murl,data=uuid)
print('------------------------------Mission 3(2)-------------------------------')
soup2=BeautifulSoup(r.text,'html.parser')
flag2=soup2.find('input')['value']
print('当前token2:%s'%flag2)

for pwd in range(0,31):
    try:
        myinfo={
        'username':'john',
        'password':pwd,
        'csrfmiddlewaretoken':flag2
                }
        r=s.post(url,data=myinfo)
        mysoup=BeautifulSoup(r.text,'html.parser')
        mytag=mysoup.find('h3')
        print(mytag.text)
        print(pwd)
    except:
        traceback.print_exc()
'''
for pwd in range(0,1):
    try:
        s=requests.Session()
        payload={
            'username':'john',
            'password':pwd
            }
        
        print(c['csrftoken'])
        r=s.post(url,data=payload,headers=header,cookies=c)
        #r=s.post(url,cookies=mycookie)
        soup=BeautifulSoup(r.text,"html.parser")
        tag=soup.find('h1')
        print(tag.text)
        print(pwd)
    except:
        traceback.print_exc()
'''
