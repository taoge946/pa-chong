
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from urllib import request
import urllib
 
mail_host="smtp.qq.com"          # 发件人邮箱中的SMTP服务器
my_sender='1169414163@qq.com'    # 发件人邮箱账号
my_pass = 'zyrzsgwbwmzthabc'              # 不是密码，是打开stmp服务的授权码
my_user='1169414163@qq.com'      # 收件人邮箱账号，我这边发送给自己

#f=open("text.html",'rb')

#msg = MIMEText(f.read(), 'html', 'utf-8')
html="""
<div class="item">
    <div class="pic">
    <em class="">1</em>
    <a href="https://movie.douban.com/subject/1292052/"> <!--影片链接-->
    <img alt="肖申克的救赎" class="" src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p480747492.jpg" width="100"/> <!--图片链接-->
    </a>
    </div>
    <div class="info">
    <div class="hd">
    <a class="" href="https://movie.douban.com/subject/1292052/"> 
    <span class="title">肖申克的救赎</span>
    <span class="title"> / The Shawshank Redemption</span>
    <span class="other"> / 月黑高飞(港)  /  刺激1995(台)</span>
    </a>
    <span class="playable">[可播放]</span>
    </div>
    <div class="bd">
    <p class="">
                                导演: 弗兰克·德拉邦特 Frank Darabont   主演: 蒂姆·罗宾斯 Tim Robbins /...<br/>
                                1994 / 美国 / 犯罪 剧情
                            </p>
    <div class="star">
    <span class="rating5-t"></span>
    <span class="rating_num" property="v:average">9.7</span>
    <span content="10.0" property="v:best"></span>
    <span>2361758人评价</span>
    </div>
    <p class="quote">
    <span class="inq">希望让人自由。</span>
    </p>
    </div>
    </div>
    </div>
"""
msg = MIMEText(html,'html','utf-8')
msg['Subject'] ="5点开会"
msg['From']=my_sender  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
msg['To']=my_user              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
#msg['Subject']="会议商讨"                # 邮件的主题，也可以说是标题

server=smtplib.SMTP_SSL(mail_host)  
server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
server.sendmail(my_sender,my_user,msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
server.quit()  # 关闭连接

