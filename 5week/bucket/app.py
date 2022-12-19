from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
client = MongoClient('mongodb+srv://tjdrkr2580:rlaxogus40@cluster0.wsngksj.mongodb.net/?retryWrites=true&w=majority')
db = client.dbspartad
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/bucket", methods=["POST"])
def bucket_post():
    bucket_receive = request.form['bucket_give']
    num = len(list(db.bucket.find({})))
    doc = {
        'num' : num,
        'name' : bucket_receive,
        'done' : 0,
    }
    print(doc)
    db.bucket.insert_one(doc)
    num = num + 1
    return jsonify({'msg': 'POST(기록) 연결 완료!'})

@app.route("/bucket/done", methods=["POST"])
def bucket_done():
    num_receive = request.form['num_give']
    db.bucket.update_one({'num': int(num_receive)},{'$set':{'done': 1}})
    return jsonify({'msg': 'POST(완료) 연결 완료!'})
# 항상 문자로 받아서 숫자로 변환

@app.route("/bucket", methods=["GET"])
def bucket_get():
    bucket_all_list = list(db.bucket.find({},{'_id' : False}))
    print(bucket_all_list)
    return jsonify(bucket_all_list)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)