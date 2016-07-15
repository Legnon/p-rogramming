# 웹툰 크롤링
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'programming.settings')
import django
django.setup()

from webtoon.models import Episode

from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests

def main():

    url_set = [ep.url for ep in Episode.objects.all()]
    print(type(url_set))
    print(url_set)
    episode_list = []

    for page in range(1,1000):
        params = {
            'titleId' : 20853,
            'page': page
        }
        page_url = 'http://comic.naver.com/webtoon/list.nhn'
        html = requests.get(page_url, params=params).text
        soup = BeautifulSoup(html, 'html.parser')
        for a_tag in soup.select('.viewList .title a'):
            title = a_tag.text
            url = urljoin(page_url, a_tag['href'])

            if url in url_set:
                print('End!')
                return episode_list

            url_set.add(url)
            print(title,url)
            episode_list.append(Episode(title=title, url=url))

print('__name__ is {}'.format(__name__))


if __name__ == '__main__':
    from django.db import connection

    episode_list = main()
    Episode.objects.bulk_create(episode_list)
    # print(connection.queries)
    # for idx, query in enumerate(connection.queries, 1):
    #     print(idx, query)
