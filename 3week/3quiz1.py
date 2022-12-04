from pymongo import MongoClient
client = MongoClient('mongodb+srv://tjdrkr2580:rlaxogus40@cluster0.wsngksj.mongodb.net/?retryWrites=true&w=majority')
db = client.dbspartad

# 가버나움 평점 가져오기
quiz1 = db.movies.find_one({'title' : '가버나움'})
result1 = quiz1['star']
print(result1)

# 가버나움의 평점과 같은 평점의 영화 제목들 가져오기
all_movies = db.movies.find({},{'_id' : False})
for movie in all_movies :
    if movie['star'] == result1 :
        print(movie['title'])

# 가버나움 0점 만들기
db.movies.update_one({'title' : '가버나움'},{'$set' : {'star' : '9.59'}})