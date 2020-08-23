# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanmoivePipeline:
    def process_item(self, item, spider):
        """
        每一个item管道都会调用此方法，并且必须返回一个item对象实例或raise DropItem异常。
        """
        # title = item['title']
        # link = item['link']
        # content = item['content']
        # output = f'|{title}|\t|{link}|\t|{content}|\n\n'
        # with open('./douban_movie.txt', 'a+', encoding='utf-8') as f:
        #     f.write(output)
        return item


class MaoyanmoivePipeline:
    def process_item(self, item, spider):
        """
        每一个item管道都会调用此方法，并且必须返回一个item对象实例或raise DropItem异常。
        """
        # title = item['title']
        # link = item['link']
        # content = item['content']
        # output = f'|{title}|\t|{link}|\t|{content}|\n\n'
        # with open('./douban_movie.txt', 'a+', encoding='utf-8') as f:
        #     f.write(output)
        return item