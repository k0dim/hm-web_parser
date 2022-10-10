import bs4
import re
import requests

def start_habr():
    ret = requests.get(URL, headers=HEADERS)
    soup = bs4.BeautifulSoup(ret.text, 'html.parser')
    articles = soup.find_all('article')
    list_start_page = []
    for article in articles:
        date = article.find('time').attrs['datetime']
        href = article.find(class_='tm-article-snippet__title-link').attrs['href']
        title = article.find(class_='tm-article-snippet__title-link').find('span').text
        start_info = {'date':date, 'href':href, 'title':title}
        list_start_page.append(start_info)
    return list_start_page

def article_page(list_start_page):
    for info in list_start_page:
        URL_PAGE = f'{URL}{info["href"]}'
        ret = requests.get(URL_PAGE, headers=HEADERS)
        soup = bs4.BeautifulSoup(ret.text, 'html.parser')
        articles = soup.find(xmlns="http://www.w3.org/1999/xhtml").text
        for word in KEYWORDS:
            word_1 = re.findall(word, articles)
            if len(word_1) >= 1:
                print(info['date'], f"{URL}{info['href']} ==> {info['title']}", sep='\n')
                print()

        

if __name__ == '__main__':
    URL = 'https://habr.com'
    HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-RU;q=0.8,en;q=0.7,en-US;q=0.6'
    }
    KEYWORDS = ['дизайн', 'фото', 'web', 'python']
    list_start_page = start_habr()
    article_page(list_start_page)