import random
import requests
from bs4 import BeautifulSoup
from bs4.element import NavigableString

prefix = 'https://www.ptt.cc{}'
url = prefix.format('/bbs/index.html')
r = requests.get(url, cookies=dict(over18='1'))
soup = BeautifulSoup(r.text, 'html.parser')
boards = [e.attrs['href'] for e in soup.find_all('a', attrs={'class': 'board'})]

board = boards[random.randint(0, len(boards))]
url = prefix.format(board)
r = requests.get(url, cookies=dict(over18='1'))
soup = BeautifulSoup(r.text, 'html.parser')

articles = [e.find('a') for e in soup.find_all('div', attrs={'class': 'r-ent'})]
articles = [article.attrs['href'] for article in articles if article]

article = articles[random.randint(0, len(articles))]
url = prefix.format(article)
r = requests.get(url, cookies=dict(over18='1'))
soup = BeautifulSoup(r.text, 'html.parser')

author, board_name, article_title, article_time = (e.string for e in soup.find_all('span', class_='article-meta-value'))

main_content = soup.find(id='main-content')
divs = main_content.find_all('div', class_='article-metaline')
anchor = divs[-1]

for e in anchor.next_siblings:
    if isinstance(e, NavigableString):
        print(e, end='')
    else:
        if e.text:
            print(e.text, end='')