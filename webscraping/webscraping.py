import requests
from bs4 import BeautifulSoup

class Webscraping():
    
    def __init__(self) -> None:
        self.url = 'https://starbucks.com/'
        pass

    def ping(self):
        print("Hello world...")

    def get_web_data(self) -> str:
        response = requests.get(self.url)
        print(response.text)
        return response.text

    def parse_html(self, html: str) -> BeautifulSoup:
        soup = BeautifulSoup(html, 'html.parser')
        return soup

        
def main():
    web_obj = Webscraping()
    web_obj.ping()
    response = web_obj.get_web_data()
    soup = web_obj.parse_html(response)
    print(soup.title)
    print(soup.title.text.strip())


if __name__ == "__main__":
    main()