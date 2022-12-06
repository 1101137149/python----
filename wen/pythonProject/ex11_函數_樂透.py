import  random

def 產生號碼(y):
    x=list()

    for n in range(1,y+1):
        x.append(n)
    return x


def 隨機抽出1號碼(x): #x=[1,2,3,4,5]
    最前項=0
    最後項=len(x)-1
    i=random.randint(最前項,最後項)
    v=x.pop(i)
    return v



    #自我挑戰
def 隨機抽出6個號碼(x):
    for n in range(6): #跑0-5
        b = 隨機抽出1號碼(a)
        c.append(b)
    return c


c=list()
a=產生號碼(42)
print(f"全部的號碼:{a}")
b=隨機抽出6個號碼(a)
print(f"抽出的號碼:{b}")
print(f"剩餘的號碼:{a}")



#抽出的從小到大排序
#d=sorted(b)
#print(f"抽出的號碼(排序):{d}")




#b=隨機抽出1號碼(a)
#print(b)
#print(a)

