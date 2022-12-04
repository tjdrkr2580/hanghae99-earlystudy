import requests #ajax 같은거래요.

r = requests.get("http://spartacodingclub.shop/sparta_api/seoulair")
rjson = r.json()

print(rjson)

rows = rjson['RealtimeCityAir']['row']

for row in rows:
    if row['IDEX_MVL'] < 60 :
        print(row['MSRSTE_NM'])
        
# 가독성이 너무 떨어진다 콘솔로 찍을 때..