a = [1,2,3,[1,2],4]
print(a[-2])

#리스트 기능

#append 덧붙이기 push 같은 기능인듯.
b = [1,2,3]
b += [2,7]
print(b)


#정렬하기
c = [1,5,3,7,9,10,2]
c.sort()
print(c)
c.sort(reverse=True)
print(c)

#요소가 리스트 안에 있는지 확인하기
d = [2,1,4,"2",6]
print(1 in d)
print("2" in d)
print(6 not in d)


#딕셔너리 - 자스 object

people = [{
    'name' : 'bob',
    'age' : 20
},{
    'name' : 'carry',
    'age' : 38
}]

person = {'name' : 'john', 'age' : 7}
people.append(person)
print(people)

people2 = [
    {'name': 'bob', 'age': 20, 'score':{'math':90,'science':70}},
    {'name': 'carry', 'age': 38, 'score':{'math':40,'science':72}},
    {'name': 'smith', 'age': 28, 'score':{'math':80,'science':90}},
    {'name': 'john', 'age': 34, 'score':{'math':75,'science':100}}
]

print(people2[2]['score']['science'])