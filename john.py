import smtplib
import email.mime.text
import email.mime.multipart
import email.mime.image 
import time
from email.mime.text import MIMEText  
msg=email.mime.multipart.MIMEMultipart()
msg['from']="xxx@163.com"
msg['to']="xxx@outlook.com"
msg['subject']="This is a test"

content="hello!"
txt=email.mime.text.MIMEText(content)
msg.attach(txt)

att=MIMEText(open('E:\\漫画\\005OIVwCjw1f1dlbpjdjlj30cs0vz762.jpg','rb').read(),'base64','utf-8')
att['Content-Type']='application/octet-stream'
att['Content-Disposition']='attachment;filename="test.jpg"'
msg.attach(att)
smtp=smtplib.SMTP()
smtp.connect('smtp.163.com')
smtp.login('name','pwd')
smtp.sendmail('xxx@163.com','xxx@outlook.com',str(msg))
smtp.quit()
#print(i)
time.sleep(2)
    
