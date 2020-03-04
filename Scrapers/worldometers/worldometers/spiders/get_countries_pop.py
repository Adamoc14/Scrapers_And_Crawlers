# -*- coding: utf-8 -*-
import scrapy
# Debug Purposes
import logging 


class GetCountriesPopSpider(scrapy.Spider):
    name = 'get_countries_pop'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        countries = response.xpath("//td/a")
        # Use the Scrapy shell command as basically youre local inspector to get what your looking for and then transfer this to this file 
        for country in countries:
            name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()

            # absolute_url = f"https://www.worldometers.info{link}"
            # absolute_url = response.urljoin(link)
            
            # yield response.follow(url=link)
            yield response.follow(url=link , callback=self.parse_country , meta={'country_name': name})
    
    def parse_country(self , response):
        # to get the name of the country , we might think of doing global variable but in our case this won't actually work and we must pass the data from our first function to the second through our meta object as such 
        name = response.request.meta['country_name']
        rows = response.xpath("(//div[@class='table-responsive'])[1]/table/tbody/tr")
        for row in rows:
            year = row.xpath(".//td[1]/text()").get()
            population = row.xpath(".//td[2]//strong/text()").get()

            yield {
                'country_name': name,
                'year': year,
                'population' : population
            }
            
