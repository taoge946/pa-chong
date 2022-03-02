from urllib import request
from bs4 import BeautifulSoup
import requests
import re

baseurl="https://www.dytt8.net"
findurl=re.compile(r'最新电影下载</a>]<a href="(.*?)">')
findname=re.compile(r'最新电影下载</a>]<a href=".*">.*《(.*?)》.*</a><br/>')
head={
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}
req=request.Request(headers=head,url="https://www.dytt8.net/index.htm")
rep=request.urlopen(req)
html=rep.read().decode('GBK')
soup=BeautifulSoup(html,"html.parser")
con=soup.select("#header > div > div.bd2 > div.bd3 > div:nth-of-type(2) > div:nth-of-type(1) > div > div:nth-of-type(2) > div.co_content8 > ul > table")
con1=str(con)
url=re.findall(findurl,con1)
name=re.findall(findname,con1)
filmurl=baseurl+url[0]

a=request.urlopen(baseurl+str(url[0]))
print(a.read().decode('GBK'))
# for i in range(len(name)):
#     #print("%s:%s\n"%(name[i],url[i]))
#     req=request.Request(headers=head,url=baseurl+url[i])
#     film=request.urlopen(req)
#     print(film.read().decode('GBK'))
