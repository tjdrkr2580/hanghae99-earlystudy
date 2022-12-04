import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('mongodb+srv://tjdrkr2580:rlaxogus40@cluster0.wsngksj.mongodb.net/?retryWrites=true&w=majority')
db = client.dbspartad

#headers 
#HTTP헤더는 클라이언트와 서버가 요청 또는 응답으로 부가적인 정보를
#전송 할 수 있게 한다.
#요청에 대한 응답을 위한 부가적인 정보

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

#headers는 get에 두 번째 인자 headers에 들어간다.

# title = soup.select_one('#old_content > table > tbody > tr:nth-child(3) > td.title > div > a')
# print(title.text)

movies = soup.select('#old_content > table > tbody > tr')

for movie in movies:
    a = movie.select_one('td.title > div > a')
    if a is not None:
        title = a.text
        rank = movie.select_one('td:nth-child(1) > img')['alt']
        star = movie.select_one('td.point').text
        doc = {
            'title' : title,
            'rank' : rank,
            'star' : star,
        }
        db.movies.insert_one(doc)


