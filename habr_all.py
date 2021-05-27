import requests as req
from bs4 import BeautifulSoup as bs


def articles_and_links():
    resp =req.get(r'https://habr.com/ru/all/')
    soup = bs(resp.text, 'html.parser')
    articles_titles = soup.findAll('a', class_='post__title_link')
    titles_links = {}
    for i in articles_titles:
        titles_links[i.text] = i.get('href')
    return titles_links
