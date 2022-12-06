import random
lotto=set()
while True:
    n=random.randint(1,42)
    lotto.add(n)
    if len(lotto)==6:
        break

print(lotto)

print("請輸入購買姓名")
name=input("名稱:")
print(f"已記錄此組號碼由{name}購買")
data=dict()
data[name]=lotto
print(data)


while True:
    key = input("查詢資料-請輸入購買姓名:")
    if key in data:
        print(f"找到{key}此筆資料{data[key]}")
        break
    elif key=="":
        print(f"已取消查詢")
        break
    else:
        print("無此人請再輸入一次，若不查詢請直接按Enter")