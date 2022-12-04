from pymongo import MongoClient
client = MongoClient('mongodb+srv://tjdrkr2580:rlaxogus40@cluster0.wsngksj.mongodb.net/?retryWrites=true&w=majority')
db = client.dbspartad

# db.users.insert_one(users) insert는 데이터 삽입
# users는 컬렉션 어느 정도 서랍에 집어넣기는 해야 하니까..
db.users.insert_one({'name' : 'yanggil', 'age' : 2})
db.users.insert_one({'name' : 'sunduk', 'age' : 1})



# find는 데이터 꺼내보기 db.컬렉션.find({} , {} <- 조건?), find_one({} <- 조건) - 하나만 꺼내기
# list 형태로 모든 데이터 뽑아보기

all_list = list(db.users.find({},{'_id' : False}))

for list_one in all_list :
    print(list_one)

user = db.users.find_one({'name' : 'taehyun'},{'_id' : False})
print(user['name'])

# 데이터 업데이트 update | 이름이 sunduk인 애를 찾아서 age를 1.5로 만들어라
db.users.update_one({'name':'sunduk'},{'$set':{'age': 1.5}})

# 데이터 삭제 delete | 조건
db.users.delete_one({'name' : 'taehyun'})
