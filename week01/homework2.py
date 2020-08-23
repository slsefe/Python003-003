"""homework 1
安装并使用 requests、bs4 库，爬取猫眼电影的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。
我选取的是猫眼电影热映口碑榜（https://maoyan.com/board/7）的前10个电影信息，包括电影名称、电影类型、电影上映时间。
"""
import time
import requests
import lxml.etree
from bs4 import BeautifulSoup
import pandas as pd

user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0'
header = {'user-agent': user_agent}


def get_url_name(url):
    """获取排行榜对应的电影详情链接"""
    response = requests.get(url, headers=header)
    selector = lxml.etree.HTML(response.text)
    film_urls = selector.xpath('//*[@class="channel-detail movie-item-title"]/a/@href')
    film_urls = ['https://maoyan.com' + film_url for film_url in film_urls]
    return film_urls[:10]


def parser_film_info(film_url):
    """从电影详情链接页面提取所需信息"""
    response = requests.get(film_url, headers=header)
    selector = lxml.etree.HTML(response.text)
    film_name = selector.xpath('//*[@class="movie-brief-container"]/h1/text()')
    print(film_name)
    film_types = selector.xpath('//*[@class="movie-brief-container"]/ul/li[1]/a/text()')
    film_types = '/'.join(type_.strip() for type_ in film_types)
    print(film_types)
    release_date = selector.xpath('//*[@class="movie-brief-container"]/ul/li[3]/text()')
    release_date = release_date[0].split(' ')[0]
    return film_name, film_types, release_date


def main():
    url = 'https://maoyan.com/films?showType=3'  # 猫眼电影热映口碑榜
    film_urls = get_url_name(url)
    film_name_list, film_type_list, release_date_list = [], [], []
    for film_url in film_urls:
        film_info = parser_film_info(film_url)
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
    maoyan_pop_films.to_csv('maoyan_pop_films.csv', index=False)


if __name__ == "__main__":
    main()
