import requests
import re
from scrapy import Selector
import pymongo
import time
from tech163.settings import MONGO_URI, MONGO_DATABASE, MONGO_COLLECTION



header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
                        '(KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
          }
url = 'http://tech.163.com/special/00094IHV/news_json.js?0.357977020453387'

def start_request(link_seen):
    MGpipeline = MongoPipeline(MONGO_URI, MONGO_DATABASE, MONGO_COLLECTION)
    html = requests.get(url, headers=header)
    result = html.text
    link_pat = re.compile(r'http://tech.163.com/\d+/\d+/\d+/\w+\.html')
    links = re.findall(link_pat, result)
    n = 0

    if links:
        try:
            MGpipeline.conn_mongodb()
            for link in links:
                if link not in link_seen:
                    parse_news(link, MGpipeline)
                    link_seen.add(link)
                    n += 1
                # else:
                #     MGpipeline.close_mongodb()
                #     print('新增内容: {}条'.format(n))
                #     return link_seen
            MGpipeline.close_mongodb()
            print('新增内容: {}条'.format(n))
            return link_seen
        except Exception as e:
            print(e)
    print('无内容')
    return link_seen


def parse_news(link, MG):
    html = requests.get(link, headers=header)
    selector = Selector(html)
    thread_pat = re.compile('.*?(\w+).html')
    item = {}
    item['news_thread'] = re.search(thread_pat, link).groups(1)[0]
    item['news_title'] = selector.css('.post_content_main h1::text').extract_first()
    item['news_url'] = link
    item['news_time'] = selector.css('.post_time_source::text').extract_first().strip()[:-4]
    item['news_from'] = selector.css('.post_time_source a::text').extract_first()
    item['from_url'] = selector.css('.left a::attr(href)').extract_first()
    item['news_content'] = selector.css('#endText p::text').extract()
    print(item)
    MG.process_item(item)



class MongoPipeline(object):

    def __init__(self, mongo_uri, mongo_db, mongo_collection):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.mongo_collection = mongo_collection


    def conn_mongodb(self):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_mongodb(self):
        self.client.close()

    def process_item(self, item):
        self.db[self.mongo_collection].update({'news_thread': item['news_thread']}, {'$set': dict(item)}, True)



if __name__ == '__main__':

    link_seen = set()

    while True:
        link_seen = start_request(link_seen)
        time.sleep(20)




