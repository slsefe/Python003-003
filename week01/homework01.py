"""homework 1
使用requests库和bs4爬取猫眼电影排行前10的电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。
"""
import time
import requests
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
    bs_info = BeautifulSoup(response.text, 'html.parser')
    film_urls = []
    for tags in bs_info.find_all('div', attrs={'class': 'channel-detail movie-item-title'}, limit=10):
        film_urls.append(tags.find('a').get('href'))
    film_urls = ['https://maoyan.com' + film_url for film_url in film_urls]
    return film_urls


def get_film_info(response):
    """从电影详情链接页面提取所需信息"""
    bs_info = BeautifulSoup(response.text, 'html.parser')
    film_info = bs_info.find('div', attrs={'class': 'movie-brief-container'})
    film_name = film_info.find('h1', attrs={'class': 'name'}).text
    li_tag = film_info.find_all('li', attrs={'class': 'ellipsis'})
    film_type = ','.join(type_.text.strip() for type_ in li_tag[0].find_all('a'))
    release_date = li_tag[2].text
    return film_name, film_type, release_date[:10]


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
    save_data(maoyan_pop_films, './maoyan_pop_films.csv')


if __name__ == "__main__":
    url = 'https://maoyan.com/films?showType=3&sortId=3'
    main(url)
