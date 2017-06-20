import random
from .agents import AGENTS



class RandomUserAgentMiddleware():
    @classmethod
    def from_crawler(cls, crawler):
        return cls()

    def process_request(self, request, spider):
        agent = random.choice(AGENTS)
        request.headers.setdefault('User-Agent', agent)


# class ProxyMiddleware():
#     # 动态设置ip代理
#     def process_request(self, request, spider):
#         get_ip = GetIP()
#         proxy = get_ip.get_random_ip()
#         request.meta["proxy"] = proxy