import urllib
import urllib.request
import re
from collections import deque

queue=deque()
visited=set()

#url_values=urllib.parse.urlencode(data)
url='http://news.dbanotes.net'
#full_url=url+url_values

queue.append(url)
cnt=0

while queue:
    url=queue.popleft()
    visited|={url}
    print('I have visited'+str(cnt)+'    I\'m visiting ----->'+url)
    cnt+=1
    urlop=urllib.request.urlopen(url,timeout=2)
    if 'html' not in urlop.getheader('Content-Type'):
        continue
    try: 
        data=urlop.read().decode('utf-8')
    except:
        continue
    linkre=re.compile('href=\"(.+?)\"')
    for x in linkre.findall(data):
        if 'http' in x and x not in visited:
            queue.append(x)
            print('add queue---->'+x)
