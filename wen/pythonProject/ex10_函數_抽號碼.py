import random

#寫個函數  接受傳入一個list
def 隨機抽(x):
    i=random.randint(0,len(x)-1)
    print(f'i={i}')
    v=x.pop(i)
    return v


#主程式
for y in range(3):  #循環3次 測試3次
    x=[10,5,3]
    v=隨機抽(x)
    print(f"結果{v}")
print() #空一格

