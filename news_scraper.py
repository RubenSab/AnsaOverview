import requests
from bs4 import BeautifulSoup
from datetime import date
from urllib.parse import urljoin

class NewsScraper:

    def __init__(self, base_url: str, selector: str):
        self.base_url = base_url
        self.selector = selector
        self.today_date = date.today().isoformat().replace('-', '/')

    def get_titles(self) -> list:
        response = requests.get(self.base_url)
        if response.status_code != 200:
            print('Failed to load the URL, Status code:', response.status_code)
            return []

        soup = BeautifulSoup(response.text, 'html.parser')
        titles_html = soup.select(self.selector)

        title_data = []
        for el in titles_html:
            title = el.get_text(strip=True)
            a_tag = el.find('a')
            if a_tag:
                relative_url = a_tag.get('href')
            absolute_url = urljoin(self.base_url, relative_url)
            title_data.append((title, absolute_url))

        titles = [
            title for title, url in title_data
            if self._was_written_today(url)
        ]
        return titles


    def _was_written_today(self, url) -> bool:
        return self.today_date in url
