def hello() :
    print('안녕')
    
hello()

def bus_rate(age) :
    if age > 65 :
        print('무료로 이용하세요.')
    elif age > 20 :
        print('성인 입니다.')
    else :
        print('청소년 입니다.')
        
bus_rate(30)
bus_rate(66)
        
# return 넣어서 결과값 돌려줄 수도 있음.

def check_gender(pin) :
    if int(pin[-7])%2 :
        print('여성')
    else :
        print('남성')
check_gender('200101-3012345')