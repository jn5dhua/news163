# news163
Scrapy+Mongodb抓取网易新闻科技频道下历史新闻(2014.3.22 - )，并实现实时监控抓取最新新闻，可复用其他网站下其他频道新闻

### http://tech.163.com/latest 科技频道滚动新闻地址
滚动新闻提供每日新闻查询和最新新闻发布，分析"往期回顾"的Ajax请求可得到api地址，api地址具有时效性

eg: http://snapshot.news.163.com/wgethtml/http+!!tech.163.com!special!00094IHV!news_json.js/2017-06/02/0.js?0.3010325175788171

### 其他频道下的滚动新闻： 替换原地址"tech"
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


