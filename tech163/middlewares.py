import random
from .agents import AGENTS



class RandomUserAgentMiddleware():
    @classmethod
    def from_crawler(cls, crawler):
        return cls()

    def process_request(self, request, spider):
        agent = random.choice(AGENTS)
        request.headers.setdefault('User-Agent', agent)

