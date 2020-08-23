# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd

class MoviesPipeline:
    def process_item(self, item, spider):
        film_name = item['film_name']
        film_types = item['film_types']
        release_date = item['release_date']
        maoyan_pop_films = pd.DataFrame(
            {
                'film_name': film_name,
                'film_types': film_types,
                'release_date': release_date
            }
        )
        maoyan_pop_films.to_csv('./maoyan_pop_films_3.csv',
                                mode='a',
                                index=False,
                                header=False)
        return item
