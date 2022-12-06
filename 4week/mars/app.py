from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb+srv://tjdrkr2580:rlaxogus40@cluster0.wsngksj.mongodb.net/?retryWrites=true&w=majority')
db = client.dbspartad

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/mars", methods=["POST"])
def web_mars_post():
    name_receive = request.form['name_give']
    address_receive = request.form['address_give']
    size_receive = request.form['size_give']
    doc = {
        'name' : name_receive,
        'address' : address_receive,
        'size' : size_receive, 
    }
    db.mars.insert_one(doc)
    return jsonify({'msg' : '주문 완료!'})

@app.route("/mars", methods=["GET"])
def web_mars_get(): 
    all_order_list = list(db.mars.find({},{'_id': False}))
    return jsonify({'orders' : all_order_list})
   

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)