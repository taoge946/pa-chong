from urllib import request 

#获取一个get请求
# response=request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))#对获取到的网页进行utf-8的译码

#获取一个post请求（post必须要服务器端有获取请求后的响应，可以使用http://httpbin.org/来进行测试）
import 
data=bytes()
response=request.urlopen("http://httpbin.org/post”）