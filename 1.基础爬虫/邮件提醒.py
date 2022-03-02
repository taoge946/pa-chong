
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
 
mail_host="smtp.163.com"          # 发件人邮箱中的SMTP服务器
my_sender='taogege946@163.com'    # 发件人邮箱账号
my_pass = 'EGVJSEOOBJJFRNAF'              # 不是密码，是打开stmp服务的授权码
my_user='1169414163@qq.com'      # 收件人邮箱账号，我这边发送给自己

msg = MIMEText("使用指南", 'html', 'utf-8')
msg = MIMEText('请查看附件内容！','plain','utf-8')
msg['Subject'] ="自动化测试报告"
msg['From']=my_sender  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
msg['To']=my_user              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
#msg['Subject']="会议商讨"                # 邮件的主题，也可以说是标题

server=smtplib.SMTP_SSL(mail_host)  
server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
server.sendmail(my_sender,my_user,msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
server.quit()  # 关闭连接
