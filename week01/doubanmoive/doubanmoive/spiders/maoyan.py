# -*- coding: utf-8 -*-
import scrapy
from lxml import etree



class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def start_requests(self):
        
        

    def parse(self, response):
        pass
