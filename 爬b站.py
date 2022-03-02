from http.client import responses
from bs4 import BeautifulSoup
import re
import urllib.request,urllib.error
from urllib import request
import xlwt
from io import BytesIO
import gzip

userid=re.compile(r'<a data-usercard-mid="(.*?)" href= .* target="_black" class="name" style="color:"></a>')

req=request.Request(url="https://www.bilibili.com/video/BV1fy4y1L7Rq",headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"})
respon=request.urlopen(req)
buff=BytesIO(respon.read())
f=gzip.GzipFile(fileobj=buff)
html=f.read().decode('utf-8')


# soup=BeautifulSoup(html,"html.parser")

# con=soup.select("#comment > div > div.comment > div > div.comment-list")
# a=con.find_all("a")
# con1=str(con)
# a=re.findall(userid,con)
print(html)

