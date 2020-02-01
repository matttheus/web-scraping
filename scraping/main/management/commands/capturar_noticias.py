from django.core.management.base import BaseCommand, CommandError
from main.models import Scraping

from bs4 import BeautifulSoup as bs
from requests import get

def get_html_parser(url):
    ''' This function get the url and return the html parsed'''

    try:
        html = get(url).text
    except Exception as err:
        print('Incorret URL or site away')
        return

    return bs(html, 'html.parser')
        
def get_news(parser, tag, class_pattern, sub_tag, sub_class_pattern):
    ''' This function get the title from the news'''

    items = parser.find_all(tag, class_=class_pattern)
    
    news = []
    for item in items:
        content = item.find('a', class_='tec--card__title__link')
        if content:
            title = item.find('a', class_=sub_class_pattern).string.strip()
            link = item.find('a', class_=sub_class_pattern).get('href')
            news.append([title, link])

    return news


class Command(BaseCommand):
    help = "This commands get news from the web"

    def handle(self, *args, **kwargs):
        try:
            html_parser = get_html_parser('https://www.tecmundo.com.br/')
            news = get_news(html_parser, 'div', 'tec--list__item', 'a', 'tec--card__title__link')
           
            for new in news:
                scraping = Scraping(title=new[0], link=new[1])
                try:
                    scraping.save()
                except:
                    pass
                
        except Exception as err:
            print(err)
            raise CommandError("Somethings went wrong")