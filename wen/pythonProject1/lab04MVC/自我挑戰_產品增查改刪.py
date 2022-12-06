from lab04MVC.自我挑戰_Model import Product

db=list()

p1=Product(1,"apple",100)
db.append(p1)


p2=Product(2,"Banana",200)
db.append(p2)


print('--所有資料--')
for p in db:
    print(p)



print('--查詢id=1--')
id=1
i=id-1
p=db[i]
print(p)

print('--修改id=1--')
id=1
i=id-1
old_p=db[i]
print('舊有資料',old_p)
new_p=Product(1,"NewApple",1000)
db[i]=new_p
print('修改成功',new_p)

print('--所有資料--')
for p in db:
    print(p)

print('--刪除id=1--')
id=1
i=id-1
p=db[i]
if p is not None:
    db[i] = None
    print('刪除成功',p)
else:
    print('刪除失敗，資料不存在')

print('--所有資料--')
for p in db:
    print(p)