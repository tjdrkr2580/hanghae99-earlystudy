from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
from pymongo import MongoClient
client = MongoClient('mongodb+srv://tjdrkr2580:rlaxogus40@cluster0.wsngksj.mongodb.net/?retryWrites=true&w=majority')
db = client.dbspartad

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    name = request.form['name']
    comment = request.form['comment']
    doc = {
        'name' : name,
        'comment' : comment,
    }
    db.m2u.insert_one(doc)
    return jsonify({'msg' : '글을 성공적으로 남겼습니다!'})

@app.route("/homework", methods=["GET"])
def homework_get():
    m2u = list(db.m2u.find({},{'_id' : False}))
    return jsonify({'m2u' : m2u})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)