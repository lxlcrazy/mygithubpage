from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

#创建一个带附件的实例
msg = MIMEMultipart()

# #构造附件1
# att1 = MIMEText(open('d:\\123.rar', 'rb').read(), 'base64', 'gb2312')
# att1["Content-Type"] = 'application/octet-stream'
# att1["Content-Disposition"] = 'attachment; filename="123.doc"'#这里的filename可以任意写，写什么名字，邮件中显示什么名字
# msg.attach(att1)

#构造附件2
att2 = MIMEText(open('e:\\123.txt', 'rb').read(), 'base64', 'gb2312')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="123.txt"'
msg.attach(att2)

#加邮件头
msg['to'] = 'fg8676@126.com'
msg['from'] = '729892005@qq.com'
msg['subject'] = 'hello world'
smtp_ser='smtp.qq.com'
#发送邮件
try:
    server = smtplib.SMTP()
    server.connect(smtp_ser,587)
    server.starttls()
    server.login('729892005@qq.com','oxmqikjzfurkbche')#XXX为用户名，XXXXX为密码
    server.sendmail(msg['from'], msg['to'],msg.as_string())
    server.quit()
    print ('发送成功')
except Exception as e:
    print (str(e))