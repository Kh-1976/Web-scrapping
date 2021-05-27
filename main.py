import requests as req
from bs4 import BeautifulSoup as bs
import re
from habr_all import articles_and_links


KEYWORDS = ['дизайн', 'фото', 'web', 'python']


def get_id_article(link):
    pattern = r'\/\d+\/'
    str = link
    post_id = re.findall(pattern, str)
    return post_id[0][1:-1]


def get_datetime(link):
    resp = req.get(link)
    soup = bs(resp.text, 'html.parser')
    return soup.find('span', class_='post__time').text


def artice_content(link):
    resp = req.get(link)
    soup = bs(resp.text, 'html.parser')
    content_article = soup.find(id='post_' + get_id_article(link))
    return content_article.find(id='post-content-body').text


def count_key_words(KEYWORDS, link):
    str = artice_content(link)
    for word in KEYWORDS:
        find_keywords = re.findall(word, str, re.I)
    return len(find_keywords)


def get_result():
    result = []
    for title, link in articles_and_links().items():
        if count_key_words(KEYWORDS, link) > 0:
            result.append([get_datetime(link), title, link])
    return result


if __name__ == '__main__':
    for datetime_title_link in get_result():
        print(datetime_title_link)
