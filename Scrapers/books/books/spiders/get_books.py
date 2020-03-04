# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class GetBooksSpider(CrawlSpider):
    name = 'get_books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ["http://books.toscrape.com"]

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//article[@class='product_pod']/div/a"), callback='parse_item', follow=True ),
        # So if you had more pages, you could make another rule under this to look for the next page link .But our website doesn't. 
        Rule(LinkExtractor(restrict_xpaths="//li[@class='next']/a")),
    )


    def parse_item(self, response):
        yield {
            'Book_Name': response.xpath("//div[@class='col-sm-6 product_main']/h1/text()").get() ,
            'Book_Price': response.xpath("//div[@class='col-sm-6 product_main']/p[1]/text()").get() 
        }
