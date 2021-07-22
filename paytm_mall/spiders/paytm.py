# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
from scrapy import Request


class PaytmSpider(scrapy.Spider):
    name = 'paytm'
    allowed_domains = ['www.paytmmall.com','paytmmall.com']
    # start_urls = ['http://www.paytmmall.com/power-bank-20000-mah-and-above-slpid']
    
    def start_requests(self):
          url="http://www.paytmmall.com/power-bank-20000-mah-and-above-slpid"
          yield SplashRequest(url)

    def parse(self, response):
        alldata=response.xpath("//div[@class='_2i1r']")
        for data in alldata:
            yield{
            'title':data.xpath(".//div[@class='_2PhD']/div[@class='UGUy']/text()").get(),
            'link' : response.urljoin(data.xpath(".//div[@class='_3WhJ']/a/@href").get()),
            'price':data.xpath(".//div[@class='_2bo3']/div[@ class='_1kMS']/span/text()").get()
            }

        next_page = response.xpath("//li[@class='_2TzX']")
        
        for page in next_page:
             absolute_page = response.urljoin(page.xpath(".//a/@href").get())
             yield scrapy.Request(url = absolute_page, callback=self.parse)



