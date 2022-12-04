import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

topRanks = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for topRank in topRanks :
    title = topRank.select_one('#body-content > div.newest-list > div > table > tbody > tr > td.info > a.title.ellipsis').text.strip()
    rank = topRank.select_one('#body-content > div.newest-list > div > table > tbody > tr > td.number').text[0:2].strip()
    artist = topRank.select_one('#body-content > div.newest-list > div > table > tbody > tr > td.info > a.artist.ellipsis').text
    print(rank, title, artist)