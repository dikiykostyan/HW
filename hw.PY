import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/catalogue/page-1.html"
top_books = []

while url:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    books = soup.select('article.product_pod')
    for book in books:
        if 'Five' in book.select_one('p.star-rating')['class']:
            title = book.h3.a['title']
            top_books.append(title)
    
    next_btn = soup.select_one('li.next > a')
    if next_btn:
        next_page = next_btn['href']
        base = "/".join(url.split('/')[:-1])
        url = f"{base}/{next_page}"
    else:
        break

with open("top_books.txt", "w", encoding="utf-8") as f:
    for title in top_books:
        f.write(title + "\n")