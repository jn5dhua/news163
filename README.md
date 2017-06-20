# news163
Scrapy+Mongodb抓取网易新闻科技频道下历史新闻(2014.3.22 - )，并实现实时监控抓取最新新闻，可复用网易新闻下其他频道新闻

## 科技频道滚动新闻地址 http://tech.163.com/latest 
网易滚动能够查询到历史新闻和新发布的新闻。可通过分析"往期回顾"的Ajax请求得到api地址，api地址具有时效性

eg: http://snapshot.news.163.com/wgethtml/http+!!tech.163.com!special!00094IHV!news_json.js/2017-06/02/0.js?0.3010325175788171

### 其他频道下的滚动新闻,替换原地址"tech":
sport:体育   
ent:娱乐       
money:财经   
auto:汽车     
mobile:手机   
digi:数码   
news:新闻

### 运行环境python3.x
main.py    启动scrapy抓取至当日数据  
monitor.py 开启监控

### 部分结果预览
![image](http://github.com/jn5dhua/news163/raw/master/images/news_list.PNG)


