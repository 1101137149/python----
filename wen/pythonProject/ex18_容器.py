print("---list[] 方括號表示---")
a=[] #list()
a.append(3.14)
a.append(100)
a.append("Hello")
print(f"a={a}")
print(f"a[0]={a[0]}")
a[0]="Tom"
print(f"a[0]={a[0]}")
########################################################
print("\n---tuple() 圓括號表示 不可修改的list---")

b=(3.14,100,"Hello")
print(f"b={b}")
print(f"b[0]={b[0]}")
print("b[0]='Tom' # tuple 是禁止修改的 執行會出錯")
# b[0]="Tom" # tuple 是禁止修改的 執行會出錯
# print(b[0])

########################################################
#讀取 打包packing裝箱
print("\n---讀取 打包packing裝箱---")
fruits=("apple","banana","cherry")
print(f"fruits={fruits}")
f1=fruits[0]
f2=fruits[1]
f3=fruits[2]
print(f"f1,f2,f3={f1} {f2} {f3}")

#簡化一行 unpacking拆箱(複製資料)
print("\n---簡化一行 unpacking拆箱(複製資料)---")
f1,f2,f3=fruits
print(f"f1,f2,f3={f1} {f2} {f3}")
print(f"fruits={fruits}")

print("\n---for迴圈 批次處理 容器資料---")
for x in fruits:
    print(f"fruits={x}")

print("\n---for迴圈 索引編號 批次處理 容器資料---")
print(f"len(fruits)={len(fruits)}")
for i in range(len(fruits)): #range(3)=>range(0,3)不含3,0~2
    #print(f"i={i}")
    print(f"第{i}項{fruits[i]}")


########################################################
print("\n---set{} 大括號表示 是無序的(代表輸出時結果順序不一定一樣)，並且不允許重複值---")

fruits={"apple","banana","cherry","apple"} #自動過濾重複值
print(f"fruits={fruits}") #順序不一定照原設定排列
print(f"len(fruits)={len(fruits)}") #3

fruits.add("芭樂") #add()新增資料
print(f"fruits={fruits}")
print(f"len(fruits)={len(fruits)}") #4

print("刪除 芭樂")
#x=fruits.remove(("芭樂")) #沒有返回值None
#print(f"x={x}")#None

fruits.remove(("芭樂"))#刪除芭樂
print(f"fruits={fruits}")

fruits.discard("芭樂")#刪除不存在的 芭樂 不會引發錯誤
#fruits.remove("芭樂") #刪除不存在的 芭樂 引發錯誤
print(f"len(fruits)={len(fruits)}") #3

#搭配try 避免引發錯誤
try:
    fruits.remove("芭樂")  # 刪除不存在的 芭樂 引發錯誤
except:
    print("fruits裡無芭樂選項，無法刪除(remove)!")

print('\n---set 放樂透號碼---')
import random
lotto=set() #set 不允許重複值
while True:
    n=random.randint(1,42)
    lotto.add(n) #自動過濾重複資料
    if len(lotto)==6:
        break
print(f"樂透開獎lotto={lotto}")


########################################################
print('\n---字典{} dict---')
#st={3.14} #set
#st={} #dict 並且有鍵和值

st=dict()
print(f"type(st)={type(st)}")

#dict{key:value,key:value....}
st={
    "name":"Tom",
    "eng": 100,
    "name": 99,
    "test":"Wendy"
}
#重複的key 會以後面的value為主
print(f"st={st}")

print('\n---dict透過 key取值---')
key="name"
print(f"key 為 name取值={st[key]}")
st={0:"Tom",1:100,2:99}
key=0
print(f"key為0取值{st[key]}")

print('\n---dict 客戶樂透資料查詢---')
#寫法1 事先建立資料
lotto={
    "Tom":{13,5,22,30,41,10},
    "Amy":{40,15,2,10,16,18}
}
print(f"lotto={lotto}")
#key =input("請輸入名字查詢樂透資料:")
key="Tom"
if key in lotto: #如果key 存在dict
    print(lotto[key]) #透過key取值
else:
    print("查無此人")

print("\n寫法2 事後建立資料")
lotto=dict()
print(f"目前配對資料lotto={lotto}")

print("\n新增 配對資料")
key="Tom"
value={13,5,22,30,41,10}
print(key)
print(value)
lotto[key]=value #key 若不存在，代表新增配對資料
print(f"目前配對資料lotto={lotto}")

print("\n新增 配對資料")
key="Amy"
value={40,15,2,10,16,18}
print(key)
print(value)
lotto[key]=value #key 若不存在，代表新增配對資料
print(f"目前配對資料lotto={lotto}")

print("\n修改 配對資料")
key="Tom"
value={1,2,3,4,5,6}
print(key)
print(value)
lotto[key]=value #key 若不存在，代表新增配對資料
print(f"目前配對資料lotto={lotto}")
