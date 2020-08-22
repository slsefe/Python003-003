"""
需求：爬取豆瓣top250电影的电影名称、上映日期和评分。
"""
import requests
from bs4 import BeautifulSoup
import lxml.etree
import pandas as pd
from tqdm import tqdm


def get_url_name(url, header):
    response = requests.get(url, headers=header)
    bs_info = BeautifulSoup(response.text, 'html.parser')
    film_urls = []
    for tags in bs_info.find_all('div', attrs={'class': 'hd'}):
        for a_tag in tags.find_all('a',):
            film_urls.append(a_tag.get('href'))
    return film_urls


def parser_film_info(film_url, header):
    response = requests.get(film_url, headers=header)
    selector = lxml.etree.HTML(response.text)
    film_name = selector.xpath('//*[@id="content"]/h1/span[1]/text()')
    plan_date = selector.xpath('//*[@id="info"]/span[10]/text()')
    rating = selector.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')
    introduction = selector.xpath('//*[@id="link-report"]/span[1]/span/text()')
    return film_name[0], plan_date[0], rating[0], introduction[0]


def main():
    user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0'
    header = {'user-agent': user_agent}
    top_250_film_urls = []
    for i in range(10):
        page_url = r'https://movie.douban.com/top250?start=%d&filter=' % (25*i)
        film_urls = get_url_name(page_url, header)
        top_250_film_urls.extend(film_urls)
    film_names, plan_dates, ratings, intros = [], [], [], []
    for film_url in tqdm(top_250_film_urls):
        film_name, plan_date, rating, intro = parser_film_info(film_url, header)
        film_names.append(film_name)
        plan_dates.append(plan_date)
        ratings.append(rating)
        intros.append(intro)
    top_250_films = pd.DataFrame({'file_name': film_names,
                                  'plan_date': plan_dates,
                                  'rating': ratings,
                                  'introduction': intros})
    top_250_films.to_csv('./douban_top_250_films.csv', encoding='utf8', index=False)


if __name__ == "__main__":
    main()
