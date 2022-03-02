import urllib
import re
import xlwt
from urllib import request,parse
from bs4 import BeautifulSoup

base_url='https://movie.douban.com/top250?start='
save_path='text.xls'
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}

findname=re.compile(r'<span class="title">(.*?)</span>')
findurl=re.compile(r'<a href="(.*?)">')
findmark=re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')
findcontent=re.compile(r'<span class="inq">(.*?)</span>',re.S)

def openurl(url):
    rep=request.Request(url=url,headers=headers)
    try:
        html=request.urlopen(rep).read().decode("utf-8")
    except OSError as e:
        if hasattr(e,"code"):
            print("错误代码:%d"%e.code)
    return html

def getdata():
    datalist=[]
    for i in range(10):
        url=base_url+str(i*25)
        html=openurl(url)
        soup=BeautifulSoup(html,"html.parser")
        for item in soup.find_all("div",class_="item"):
            item=str(item)
            data=[]
            name=re.findall(findname,item)[0]
            data.append(name)

            link=re.findall(findurl,item)[0]
            data.append(link)

            mark=re.findall(findmark,item)[0]
            data.append(mark)

            content=re.findall(findcontent,item)
            data.append(content)

            datalist.append(data)
    return datalist

def savedata(data,savepath):
    book=xlwt.Workbook(encoding='utf-8')
    sheet=book.add_sheet("sheet1")
    col=("名称","链接","评分","简介")
    for i in range(4):
        sheet.write(0,i,col[i])
        for j in range(250):
            sheet.write(j+1,i,data[j][i])
    book.save(save_path)
    print("数据爬取完毕")

if __name__=='__main__':
    savedata(getdata(),save_path)
    #print(getdata()[1][1])