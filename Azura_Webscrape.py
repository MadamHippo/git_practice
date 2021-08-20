from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

my_url = "https://azurajewelry.com/collections/all-products"

# Azura Jewelry = Product | Price | Rating

request_page = urlopen(my_url)
page_html = request_page.read()
request_page.close()

html_soup = soup(page_html, 'html.parser')
azura_items = html_soup.find_all("div", class_="indiv-product")

filename = "azura_scrape.csv"
f = open(filename, "w")
headers = "Title, Price, Rating \n"

f.write(headers)


for product in azura_items:
    title = product.find("span", class_="indiv-product-title-text").text
    price = product.find("span", class_="money").text
    rating = product.find("span", class_="stamped-badge")['data-rating']

    f.write(title + "," + price + "," + rating + "\n")

    print("Title:" + title + " | ")
    print("Price:" + price  + " | ")
    print("Rating:" + rating + " | ")

f.close()