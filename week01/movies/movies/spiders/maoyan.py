# -*- coding: utf-8 -*-
import scrapy
from movies.items import MoviesItem
from scrapy.selector import Selector


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3&sortId=3']

    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3&sortId=3'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        film_urls = Selector(response=response).xpath(
            '//div[@class="channel-detail movie-item-title"]/a/@href').extract()
        film_urls = ['https://maoyan.com' + film_url for film_url in film_urls[:10]]
        for film_url in film_urls:
            yield scrapy.Request(url=film_url, callback=self.parse2)
    
    def parse2(self, response):
        item = MoviesItem()
        film_info = Selector(response=response).xpath(
            '//div[@class="movie-brief-container"]')
        film_name = film_info.xpath('./h1/text()').extract()
        film_types = film_info.xpath('./ul/li[1]/a/text()').extract()
        film_types = '/'.join(type_.strip() for type_ in film_types)
        release_date = film_info.xpath('./ul/li[3]/text()').extract()
        item['film_name'] = film_name
        item['film_types'] = film_types
        item['release_date'] = release_date[:10]
        yield item


