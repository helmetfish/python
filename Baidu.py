import requests
from bs4 import BeautifulSoup
import re
import django
murl='https://www.baidu.com'
lurl='https://passport.baidu.com/v2/api/?login'
turl='https://passport.baidu.com/v2/api/?getapi&class=login&tpl=mn&tangram=true'
tieba='http://tieba.baidu.com/f?ie=utf-8&kw=%E5%9B%BD%E9%99%85%E7%B1%B3%E5%85%B0'
def mylogin(uname,pwd):
    s.get(murl)
    s.get(lurl)
    rtoken=s.get(turl).text
    token=re.findall("bdPass.api.params.login_token='(.*?)'",rtoken)[0]
    print(token)
    payload={
        'username':uname,
        'password':pwd,
        'token':token,
        'verifycode':''
        }
    headers = {
    'Host': 'passport.baidu.com',
    "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:27.0) Gecko/20100101 Firefox/27.0",
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://pan.baidu.com/',
    'Content-Type': 'application/x-www-form-urlencoded'
    }
    s.get(lurl,headers=headers)
#验证码
    login=s.post(lurl,data=payload,headers=headers)
    get_code=re.findall("codestring=(.*?)&username",login.text)[0]
    print(get_code)
    code=s.get('https://passport.baidu.com/cgi-bin/genimage',params=get_code,stream=True)
    path="E:/newcode.jpg"    
    if code.status_code==200:
        with open(path,'wb') as f:
            for ch in code.iter_content():
                f.write(ch)
            
    verifycode=''
    while not verifycode:
        verifycode=input("输入验证码：")
        print(verifycode)

    payload={
        'token' : token,
        'codestring' : get_code,
        'username': uname,
        'password': pwd,
        'verifycode':verifycode,
            #'mem_pass':'on',
        }
    login2=s.post(lurl,data=payload,headers=headers)
    print(s.cookies)
    if 'BDUSS' in s.cookies:
        print(" 登录成功")
    else:
        print("登录失败")
if __name__=='__main__':
    s=requests.Session()
    mylogin('name','pwd')

