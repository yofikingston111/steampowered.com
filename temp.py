import requests
from bs4 import BeautifulSoup


class Scraper:

    def __init__(self, url: str):
        self.url = url

    def get_data(self):
        r = requests.get(self.url)
        return r.text

    def parse(self, data):
        result = []  # <- append sorting data

        soup = BeautifulSoup(data, 'html.parser')
        contents = soup.find('div', attrs={'id': 'search_resultsRows'})
        games = contents.find_all('a')
        for game in games:
            link = game['href']

            # parsing data
            title = game.find('span', {'class': 'title'}).text
            price = game.find('div', {'class': 'search_price'}).text.strip().split('£')

            # sorting
            data_dict = {
                'title': title,
                'price': price,
                'link': link
            }

            # append
            result.append(data_dict)
        return result

    # process cleaned data from parser
    def output(self, datas: list):
        for i in datas:
            print(i)


class Indeed(Scraper):
    pass

if __name__ == '__main__':
    url = 'https://store.steampowered.com/search/?term=dota'
    scraper = Indeed(url)
    data = scraper.get_data()
    parse = scraper.parse(data)
    scraper.output(parse)
