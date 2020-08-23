# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from doubanmoive.items import DoubanmoiveItem

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    # def parse(self, response):
    #     pass

    def start_requests(self):
        """
        爬虫启动时，引擎自动调用该方法，并且只会被调用一次，用于生成初始的请求对象。
        start_requests()方法读取start_urls列表中的URL并生成Request对象，发送给引擎。
        引擎再指挥其他组件向网站服务器发送请求，下载网页。
        """
        for i in range(10):
            url = 'https://movie.douban.com/top250?start=%d&filter='%(i*25)
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        title_list = soup.find_all('div', attrs={'class': 'hd'})
        for i in title_list:
            title = i.find('a').find('span').text
            link = i.find('a').get('href')
            item = DoubanmoiveItem()
            item['title'] = title
            item['link'] = link
            yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2)

    def parse2(self, response):
        item = response.meta['item']
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.find('div', attrs={'class': 'related-info'}).get_text().strip()
        item['content'] = content
        yield item

