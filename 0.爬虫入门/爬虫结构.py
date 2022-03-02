#coding=utf-8
from http.client import responses
from bs4 import BeautifulSoup
import re
import urllib.request,urllib.error
import xlwt
import sqlite3

baseurl="https://movie.douban.com/top250?start="
save_path="豆瓣电影top250.xls"

findlink=re.compile(r'<a href="(.*?)">') #通过网页中电影链接的规律定义正则表达式来获取链接,括号为所要提取的内容
findimageSrc=re.compile(r'<img.*src="(.*?)"',re.S) #re.S表示忽略这里面的换行符,可能网址中就有\n,所以要加
findtitle=re.compile(r'<span class="title">(.*?)</span>')#提取出影片的片名
findrating=re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')#抓取出评分
findjudge=re.compile(r'<span>(\d*?)人评价</span>')#抓取出评分认识，\d在正则中表示数字
findInq=re.compile(r'<span class="inq">(.*?)</span>')#抓取评价
findBd=re.compile(r'<p class="">(.*?)</p>',re.S)#抓取影片的相关内容，内容有换行符所以必须加re.S

#具体步骤为
# 1.爬取网页
# 2.逐一解析数据     一般是边爬取边解析的
# 3.保存数据

def main():
    baseurl="https://movie.douban.com/top250?start="#网址后面接一个问号？意味着接下来的都是网页的参数了。
                                                    #根据本次网址的命名规律我们可以知道根据start=n的数值不同，从n+1开始显示
    save_path=""
    datalist=get_data(baseurl)
    save_data(datalist,save_path)

def get_data(baseurl):      #获取网页上的数据
    datalist=[]
    for i in range(0,10):
        url=baseurl+str(i*25)
        html=askURL(url) #获取到前250的电影的所有内容
        #逐一解析
        soup=BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_="item"):  #查找符合要求的字符串，形成列表   class是类别，要加下划线，表示的是属性值
            #print(item) #测试查看电影item所有信息                               #在本例中就是要找到每个电影的内容并进行拆分。
            data=[] #保存这一部电影的所有信息
            item=str(item)  #变成字符串比较好处理，接下来就可以用正则表达式对字符串进行操作了
            link=re.findall(findlink,item)[0] #不要列表形式的，要数组形式的，要其中的内容
            data.append(link)

            imgSRC=re.findall(findimageSrc,item)[0]
            data.append(imgSRC)

            titles=re.findall(findtitle,item) #通过观察网页可以得知有的影片有中文名字和外文名字，而有的只有一个名字，所以给他分开。
                                              #有多个内容时就不加[0]了
            if len(titles)==2 :
                zh_title=titles[0]
                data.append(zh_title)
                en_title=titles[1].replace("/","")#外文名字前有个"/"给他去掉
                data.append(en_title)
            else:
                data.append(titles[0])
                data.append(" ") #没有外文名字就用空格替代  
            
            rating=re.findall(findrating,item)[0]
            data.append(rating)

            judgeNum=re.findall(findjudge,item)[0]
            data.append(judgeNum)

            inq=re.findall(findInq,item)  #有的影片没有概述，所以不加[0]再判断一下
            if len(inq)!=0:
                inq=inq[0].replace("。","")#去掉句号
                data.append(inq)
            else:
                data.append("") #没有就留空

            bd=re.findall(findBd,item)[0]
            bd=re.sub('<br(\s+)?/>(\s+)?',"",bd)#使用正则表达式去掉<br/>,[\S]---表示，非空白就匹配,就是说如果有其他内容也一块替换掉
            data.append(bd.strip()) #用.strip()去掉bd内容前后的空格

            datalist.append(data) #吧处理好的一部电影放到datalist中去
    #print(datalist)
    return datalist

def save_data(datalist,save_path):
    workbook=xlwt.Workbook(encoding="utf-8")
    worksheet=workbook.add_sheet("豆瓣电影top250",cell_overwrite_ok=True)
    col=('电影详情链接','图片链接','影片中文名','影片外文名 ','评分','评价数','概况','相关信息')
    for i in range(8):
        worksheet.write(0,i,col[i]) #写入列名
    for i in range(250):
        print("正在准备写入第%d条"%i)
        data=datalist[i]
        for j in range(8):
            worksheet.write(i+1,j,data[j])
    workbook.save(save_path)

def askURL(url):
    print("开始爬取豆瓣服务器")
    head={  #用户代理，告诉服务器你不是爬虫是一个正常的浏览器，
        "User-Agent":" Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
    }
    rep=urllib.request.Request(url=url,headers=head)
    html=''
    try :
        response=urllib.request.urlopen(rep)
        html=response.read().decode('utf-8')
        #print(html)
    except urllib.error.URLError as e:  #打不开网页的错误
        if hasattr(e,"code"):  #如果错误e有code这个属性就打印出来，如418,404等
            print (e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html

if __name__=="__main__":
    datalist=get_data(baseurl)
    save_data(datalist,save_path)