import requests as requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.1iypvdi.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

client = MongoClient('mongodb+srv://test:sparta@cluster0.1iypvdi.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

for i in range (1,6):
    url = 'https://first-man.tistory.com/?page='+str((i))

    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    blogs = soup.select('#container > main > div > div.area-common > article')

    for blog in blogs:
        a = blog.select_one('strong')
        if a is not None:
            title = a.text
            time = blog.select_one('div > span.date').text
            summary = blog.select_one('div > a > p').text
            print(title, time, summary)
            

            
