from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('mongodb+srv://tjdrkr2580:rlaxogus40@cluster0.wsngksj.mongodb.net/?retryWrites=true&w=majority')
db = client.dbspartad
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/movie", methods=["POST"])
def movie_post():
    url = request.form['url']
    star = request.form['star']
    comment = request.form['comment']
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url,headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    title = soup.select_one('div.mv_info > h3 > a').text
    desc = soup.select_one('div.story_area > p').text
    img = soup.select_one('div.poster > a > img')['src']
    doc = {
        title,
        img,
        star,
        comment,
        desc,
    }
    db.movies.insert_one(doc)
    return jsonify({'msg' : '평을 정상적으로 남겼습니다!'})

@app.route("/movie", methods=["GET"])
def movie_get():
    all_movie_list = list(db.movies.find({},{'_id' : False}))
    return jsonify({'movies' : all_movie_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)