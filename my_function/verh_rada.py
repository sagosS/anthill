from bs4 import BeautifulSoup
from my_class import get_html

url_query: str = 'https://iportal.rada.gov.ua/ru/news'
url_read = get_html.GetHTML()

if url_read:
    soup = BeautifulSoup(url_read.get_html(url_query), "html.parser")
    news = soup.findAll("p")
    news_item = soup.find("div", id="list_archive")
    date_news = news_item.findAll("span", class_='date')
    text_news = news_item.findAll("p")
    link_news = news_item.findAll("a", href=True)

    while date_news:
        print(date_news[0].text)
        print(text_news[0].text)
        print(url_query+link_news[0]['href'])
        print()
        del(date_news[0])
        del(text_news[0])
        del(link_news[0])
else:
    print("Error Read URL")
