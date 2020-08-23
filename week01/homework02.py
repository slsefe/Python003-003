"""homework 1
使用requests库和xpath爬取猫眼电影排行前10的电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。
"""
import time
import requests
import lxml.etree
from bs4 import BeautifulSoup
import pandas as pd

user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0'
header = {'user-agent': user_agent}


def get_response(url):
    """请求网页"""
    try:
        response = requests.get(url, headers=header)
        return response
    except Exception as e:
        raise e

def get_film_urls(response):
    """获取排行榜对应的电影详情链接"""
    selector = lxml.etree.HTML(response.text)
    film_urls = selector.xpath('//*[@class="channel-detail movie-item-title"]/a/@href')
    film_urls = ['https://maoyan.com' + film_url for film_url in film_urls[:10]]
    return film_urls


def get_film_info(response):
    """从电影详情链接页面提取所需信息"""
    selector = lxml.etree.HTML(response.text)
    film_name = selector.xpath('//*[@class="movie-brief-container"]/h1/text()')
    film_types = selector.xpath('//*[@class="movie-brief-container"]/ul/li[1]/a/text()')
    film_types = '/'.join(type_.strip() for type_ in film_types)
    release_date = selector.xpath('//*[@class="movie-brief-container"]/ul/li[3]/text()')
    release_date = release_date[0].split(' ')[0]
    return film_name[0], film_types, release_date[:10]


def save_data(df, file_path):
    """保存dataframe结果到指定文件"""
    df.to_csv(file_path, index=False)


def main(url):
    response = get_response(url)
    film_urls = get_film_urls(response)
    film_name_list, film_type_list, release_date_list = [], [], []
    for film_url in film_urls:
        response = get_response(film_url)
        film_info = get_film_info(response)
        film_name_list.append(film_info[0])
        film_type_list.append(film_info[1])
        release_date_list.append(film_info[2])
        time.sleep(1)
    maoyan_pop_films = pd.DataFrame(
        {
            'film_name': film_name_list,
            'film_type': film_type_list,
            'release_date': release_date_list
        }
    )
    save_data(maoyan_pop_films, './maoyan_pop_films_2.csv')



if __name__ == "__main__":
    url = 'https://maoyan.com/films?showType=3&sortId=3'
    main(url)
