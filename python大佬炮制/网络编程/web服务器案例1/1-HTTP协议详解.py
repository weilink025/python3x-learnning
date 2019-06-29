"""
HTTP请求方式：

GET 获取数据
POST 修改数据
PUT  保存数据
DELETE 删除
OPTION  询问服务器某种支持特性
HEAD   返回报文头

General

Request URL: http://wuyoubaotech.com/
Request Method: GET
Status Code: 200 OK
Remote Address: 47.106.165.38:80
Referrer Policy: no-referrer-when-downgrade

Request Hearders

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8   #指定客户端能够接收的内容类型
Accept-Encoding: gzip, deflate   #指定浏览器可以支持的web服务器返回内容压缩编码类型。
Accept-Language: zh-CN,zh;q=0.9     #浏览器可接受的语言
Cache-Control: no-cache            #指定请求和响应遵循的缓存机制
Connection: keep-alive          #示是否需要持久连接。（HTTP 1.1默认进行持久连接）
Host: wuyoubaotech.com        #指定请求的服务器的域名和端口号
Pragma: no-cache              #用来包含实现特定的指令
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36   #用户信息


Respones Hearders


Accept-Ranges: bytes     #表明服务器是否支持指定范围请求及哪种类型的分段请求
Connection: Keep-Alive
Content-Encoding: gzip    #压缩编码
Content-Length: 287      #响应体的长度
Content-Type: text/html     #返回内容的MIME类型
Date: Thu, 27 Jun 2019 13:25:24 GMT
ETag: "7c0240-17d-584f7bd62ddc2"     # 请求变量的实体标签的当前值
Keep-Alive: timeout=15, max=300
Last-Modified: Tue, 26 Mar 2019 04:27:32 GMT    #请求资源的最后修改时间
Server: Apache
Vary: Accept-Encoding,User-Agent    # 告诉下游代理是使用缓存响应还是从原始服务器请求


"""