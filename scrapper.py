import random
import requests

from bs4 import BeautifulSoup

BASE_URL  = 'https://en.wikipedia.org'

def scrapper(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find(id='firstHeading')
        print(title.text)
        all_links = soup.find(id='bodyContent').find_all('a')
        random.shuffle(all_links)
        linkToScrape = 0
        for link in all_links:
            if link['href'].find('/wiki/') == -1:
                continue
            linkToScrape = link['href']
            break
        scrapper(f'{BASE_URL}/{linkToScrape}')
    else:
        print('Something went wrong')


if __name__ == '__main__':
    URL = f'{BASE_URL}/wiki/Web_scraping'
    scrapper(URL)