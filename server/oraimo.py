import requests
from bs4 import BeautifulSoup
import pandas as pd


# Specify the CSV file name


# Send request and parse HTML
book_list =[]
for i in range(1,6):
    html_text = requests.get(f'https://gh.oraimo.com/oraimo-daily-deals.html?utm_source=google&utm_medium=google%2Fcpc&campaignid=20229148690&kwd=oraimo%20store&gad_source=1&gclid=Cj0KCQiA84CvBhCaARIsAMkAvkK_2JvDhdVmZlefo9N0HYBhLRPq-n8zYt8bII-qhD5cmFI2vPYObIoaAh-cEALw_wcB&page={i}').text
    soup = BeautifulSoup(html_text, 'lxml')

    category_list = soup.find_all('div', class_='site-product')

   
    iteration = 1
    for list in category_list:
        price = list.find('p', class_='product-price').span.text.strip()
        name = list.h3.text.strip()
        book_list.append([name,price])
        iteration +=1


df = pd.DataFrame(book_list, columns = ['product name','price'])
df.to_csv('oraimo_prices.csv')