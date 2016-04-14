import urllib.request
import gzip
import re
import http.cookiejar
import urllib.parse

def unzip(data):
    try:
        print('正在解压...')
        data=gzip.decompress(data)
        print('解压完成')
    except:
        print('未经压缩，无需解压')
    return data
def getXSRF(data):
    cer=re.compile('name=\"_xsrf\" value=\"(.*)\"',flags = 0)
    strlist=cer.findall(data)
    return strlist[0]

url='http://www.zhihu.com'

def save_file(data):
    file=open('E:\\save.txt','wb')
    file.write(data)
    file.close()

def Opener(head):
    cj=http.cookiejar.CookieJar()
    pro=urllib.request.HTTPCookieProcessor(cj)
    opener=urllib.request.build_opener(pro)
    header=[]
    for key,value in head.items():
        elem=(key,value)
        header.append(elem)
    opener.addheaders=header
    return opener

header = {
    'Connection': 'Keep-Alive',
    'Accept':'text/html, application/xhtml+xml,*/*',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586',
    'Accept-Language':'zh-Hans-CN,zh-Hans;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'www.zhihu.com',
    'DNT': '1'
}
'''    
request=urllib.request.Request(url,headers={
     'Connection':'Keep-Alive',
     'Accept': 'text/html, application/xhtml+xml, */*',
     'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
     'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'  
    })
'''
url = 'http://www.zhihu.com/'
opener=Opener(header)
op=opener.open(url)
data=op.read()
data=unzip(data)
_xsrf = getXSRF(data.decode())

url+='login/phone_num'
id='phonenumber'
password='password'
postDict={
    '_xsrf':_xsrf,
    'phone_num':id,
    'password':password
    }
postData=urllib.parse.urlencode(postDict).encode()
op=opener.open(url, postData)
data=op.read()
print(data)
data=unzip(data)
print(data.decode('utf-8'))

