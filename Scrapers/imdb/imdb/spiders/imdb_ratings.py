# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ImdbRatingsSpider(CrawlSpider):
    name = 'imdb_ratings'
    allowed_domains = ['imdb.com']

    userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.7 Safari/537.36'

    def start_requests(self):
        yield scrapy.Request(url="https://www.imdb.com/chart/top/?ref_=nv_mv_250", headers ={
            'User-Agent': self.userAgent
        })

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//td[@class="titleColumn"]/a'), callback='parse_item', follow=True , process_request='set_request_headers'),
        # So if you had more pages, you could make another rule under this to look for the next page link .But our website doesn't. 

        # So what if the website thinks you're a bot , you need to change your headers in the request . To do this , just change the above statement to include a process_request paramater which states
        # that all the request be handled by a specific callback function called set_request_headers(self)  like below
    )

    def set_request_headers(self , request):
        request.headers['User-Agent'] = self.userAgent
        return request

    def parse_item(self, response):
        yield {
            'title': response.xpath("//div[@class='title_wrapper']/h1/text()").get(),
            'year': response.xpath("//span[@id='titleYear']/a/text()").get(),
            # to know why i did this take out normalize-space and run it again 
            'duration': response.xpath("normalize-space(//time/text())").get(),
            'genre': response.xpath("//div[@class='subtext']/a[1]/text()").get(),
            'movie_rating_value': response.xpath("//span[@itemprop='ratingValue']/text()").get(),
            'possible_rating_value': response.xpath("//div[@class='ratingValue']/span[2]/text()").get(),
            'movie_url': response.url
        }
