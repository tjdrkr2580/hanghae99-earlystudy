money = 4900
if money == 5000 :
    print("dddd")
else :
    print('tttt')
    
# 자스랑은 다르게 !==가 안되는듯 *문자형까지는 비교가 안되는듯*

fruits = ['사과','배','감','귤']

for fruit in fruits :
    print(fruit)
    
people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby', 'age': 57},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 25}
]

for person in people :
    if person['age'] > 20 :
        print(person['name'])
        
#enumerate 
#반복문 사용 시 몇 번째 반복문인지 확인이 필요할 수 있음.
#인덱스 번호와 컬렉션의 원소를 tuple 형태로 반환합니다.
#i를 사용할 수 있게 됨.

for i, fruit in enumerate(fruits) :
    print(i, fruit)
    if i == 4 :
        break

num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]

for num in num_list :
    if num % 2 == 0 :
        print(num)
count = 0

for num in num_list :
    if num % 2 == 0 :
        count += 1
print(count)

max_num = 0
for num in num_list :
    if max_num < num :
        max_num = num
print(max_num)

print(max(num_list))