# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_splash import SplashRequest


class GetGarageDetSpider(CrawlSpider):
    name = 'get_garage_det'
    allowed_domains = ['www.simi.ie']

    script = """
        function main(splash)
            assert(splash:wait(50000))
            assert(splash:go(splash.args.url))
            return splash:evaljs("document.title")
        end
    """

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//a[@class="MemberCard__go Button Button--orange Button--inline"]'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths='//a[@class="MemberSearch__pagination-link"]')),
    )
   
    start_urls = ['https://www.simi.ie/en/find-a-member']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse_item, endpoint='execute', args={'lua_source': self.script})

    def parse_item(self, response):
        yield {
            'Garage_Name': response.xpath("//span[@class='Heading__text']/text()").get(),
            'Garage_Address': response.xpath("//div[@class='MemberCard__contact-row'][1]/text()").get(),
            'Garage_Number': response.xpath("//div[@class='MemberCard__contact-row'][2]/span/text()").get(),   
        }
