# -*- coding: utf-8 -*-
import scrapy
import re
import datetime
from tech163.items import Tech163Item
from scrapy.spiders import Spider, Request


class A163Spider(Spider):
    name = 'news'
    allowed_domains = ['http://snapshot.news.163.com', 'tech.163.com']
    startYear = '2014'    #最早只能查询到2014.3.22的新闻
    startMonth = '03'
    startDay = '22'
    dtnow = datetime.datetime.now()
    api_news_url = 'http://snapshot.news.163.com/wgethtml/http+!!tech.163.com!special!00094IHV!news_json.js/{}-{}/{}/0.js?0.3010325175788171'
    link_pat = re.compile(r'http://tech.163.com/\d+/\d+/\d+/\w+\.html')

    def start_requests(self):
        yield Request(self.api_news_url.format(self.startYear, self.startMonth, self.startDay),
                      meta={'Year': self.startYear, 'Month': self.startMonth, 'Day': self.startDay})


    def parse(self, response):
        links = re.findall(self.link_pat, response.text)
        for link in links:
            yield Request(link, callback=self.parse_news)

        Year = response.meta['Year']
        Month = response.meta['Month']
        Day = response.meta['Day']
        #转换为时间类型自增
        s = '{}-{}-{}'.format(Year, Month, Day)
        dt = datetime.datetime.strptime(s, '%Y-%m-%d')
        dt = dt + datetime.timedelta(days=1)
        if dt <= self.dtnow:
            Year = str(dt)[0:4]
            Month = str(dt)[5:7]
            Day = str(dt)[8:10]
            yield Request(self.api_news_url.format(Year, Month, Day), dont_filter=True,
                          meta={'Year': Year, 'Month': Month, 'Day': Day})

    def parse_news(self, response):
        item = Tech163Item()
        thread_pat = re.compile('.*?(\w+).html')
        item['news_thread'] = re.match(thread_pat, response.url).groups(1)[0]   #新闻id
        item['news_title'] = response.css('.post_content_main h1::text').extract_first()
        item['news_url'] = response.url
        item['news_time'] = response.css('.post_time_source::text').extract_first().strip()[:-4]
        item['news_from'] = response.css('.post_time_source a::text').extract_first()   #新闻来源
        item['from_url'] = response.css('.left a::attr(href)').extract_first()  #来源网站
        item['news_content'] = response.css('#endText p::text').extract()

        return item
