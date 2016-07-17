# 포켓몬 도감 크롤링
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'programming.settings')
import django
django.setup()

from pokemon.models import Pokemon_crawling

from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests

def main():
    url_set = {pk.url for pk in Pokemon_crawling.objects.all()}
    poke_list = []
    for page in range(1,41):
        params = {
            'page': page
        }
        page_url = 'http://pokedex.pokemonkorea.co.kr/'
        html = requests.get(page_url, params=params).text
        soup = BeautifulSoup(html, 'html.parser')
        for td in soup.select('#MonList .list .td'):
            name = td.select('.td_title h4')[0].text
            url = urljoin(page_url, 'templates/default/'+td.select('.td_body img')[0]['src'])

            if url in url_set:
                print('End!')
                return poke_list

            url_set.add(url)
            print(name,url)
            poke_list.append(Pokemon_crawling(name=name, url=url))
    return poke_list

if __name__ == '__main__':
    poke_list = main()
    print(poke_list)
    Pokemon_crawling.objects.bulk_create(poke_list)
    # Pokemon.objects.all().delete()

