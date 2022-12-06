import random #載入程式模組(.py)
n=random.randint(1,3) #隨機產生 範圍數字 ex 從1~3的範圍  隨機產生一個數字
print(n)

#a=[1,2,3,4,5]      # 列表第一種寫法
a=list((1,2,3,4,5)) # 列表第二種寫法
print(a)
print(f"長度 {len(a)}")

i=random.randint(1,4) #亂數決定 抽1~4項
print(f"抽出i項{i}")

v=a.pop(i) #取得刪除的項目
print(f"值{v}被抽出了!")
print(a)
print(f"長度{len(a)}")

print("------------------------")



#練習樂透1~42 抓6個數 還沒寫完

c=list()
a=random.randint(1, 42)
c.append(a)
#print(len(c))
for q in range(1,6) :
    a = random.randint(1, 42)
    b = True

    # 檢核重複 就移除
    for i in c:
        if a == i:
            b=False
        else:
            pass
            #print(i)

    if b!=False :
        c.append(a)
print(c)



