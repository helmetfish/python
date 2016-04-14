import urllib.request
import re

url='http://www.baidu.com'
data=urllib.request.urlopen(url)
data=data.read()
print(data)
