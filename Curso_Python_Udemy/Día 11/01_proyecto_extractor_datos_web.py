import bs4
import requests

url_base = "https://books.toscrape.com/catalogue/category/books_1/page-{}.html"

for n in range(1, 11):
    web = requests.get(url_base.format(n))
    sopa = bs4.BeautifulSoup(web.text, "lxml")
    for libro in sopa.select(".product_pod"):
        if libro.select(".star-rating.Four"):
            print(f"'{libro.select("a")[1]["title"]}' este libro tiene 4 estrellas")
        elif libro.select(".star-rating.Five"):
            print(f"'{libro.select("a")[1]["title"]}' este libro tiene 5 estrellas")
