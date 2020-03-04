# -*- coding: utf-8 -*-
import scrapy


class GetGlassesDetailsSpider(scrapy.Spider):
    name = 'get_glasses_details'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['https://www.glassesshop.com/bestsellers']

    def parse(self, response):
        glasses = response.xpath("//div[@class='prlist row']/div")
        for glass_det in glasses:
            url = glass_det.xpath(".//div[contains(@class, 'row')]/p/a/@href").get()
            image_url  = glass_det.xpath(".//div[@class='pimg default-image-front']/a/img[1]/@src").get()
            product_name = glass_det.xpath(".//div[contains(@class, 'row')]/p/a/text()").get()
            product_price = glass_det.xpath(".//div[@class='pprice col-sm-12']/span/text()").get()
        
            yield {
                'Product_URL' : url,
                'Image_URL': image_url,
                'Product_Name': product_name,
                'Product_Price': product_price
            }

        next_page = response.xpath("//ul[@class='pagination']/li[position() = last()]/a/@href").get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)

