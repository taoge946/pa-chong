import urllib
from urllib import request
import re
from bs4 import BeautifulSoup
import os

findimageSrc=re.compile(r'<img.*src="(.*?)"',re.S)
baseurl="https://movie.douban.com/top250?start="
head={  
        "User-Agent":" Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
    }
rep=request.Request(url=baseurl,headers=head)
html=request.urlopen(rep).read().decode('utf-8')
imgurl=[]
soup=BeautifulSoup(html,'html.parser')
for item in soup.find_all("div",class_="item"):
    item=str(item)
    imgurl.append(re.findall(findimageSrc,item)[0])
for i in range(len(imgurl)):
    req=request.Request(url=imgurl[i],headers=head)
    imgdata=request.urlopen(req).read()
    image_name=str(i)+'.jpg'
    with open(image_name,'wb') as f: #不用先创建一个空文件，直接这么写入就会自动创建
        f.write(imgdata)
        f.close