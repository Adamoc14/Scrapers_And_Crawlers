# -*- coding: utf-8 -*-
import scrapy


class GdpDebtSpider(scrapy.Spider):
    name = 'gdp_debt'
    allowed_domains = ['worldpopulationreview.com']
    start_urls = ['http://worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        countries = response.xpath("//table[@class='table table-striped']/tbody/tr")
        for country in countries:
            name = country.xpath(".//td[1]/a/text()").get()
            debt = country.xpath(".//td[2]/text()").get()
            population = country.xpath(".//td[3]/text()").get()

            yield {
                'Year' : 2019,
                'Country_Name': name,
                'National Debt to GDP Ratio': debt,
                'Country_Population': population
            }
