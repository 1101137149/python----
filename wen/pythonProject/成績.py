import random

#跑列表用函數
def 產出列表(num):
    v = list()
    for i in range(0,num+1):
       v.append(i)

    return v

score=產出列表(100)

print(score)
scorelist=list(); #全部成績列表
goodlist = list(); #及格列表
badlist=list(); #不及格列表

for i in range(1,11):
    a = random.randint(0, len(score) - 1)  # 亂數決定 抽列表裡的數字
    v = score.pop(a)
    scorelist.append(v)
    if v >= 60:
        goodlist.append(v)
    else:
        badlist.append(v)

print(f"全部={scorelist}")
print(f"及格={goodlist}")
print(f"不及格={badlist}")








