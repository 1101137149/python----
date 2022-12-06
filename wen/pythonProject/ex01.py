print("Hello World!") #輸出結果
type("Hello World!") #查詢型態
print(type("Hello World!")) #str
print(type(100)) #int
print(type(1.2)) #float

print("----------------------------")
# 定義變數
n ="Wendy"
e=100
m=99
t=e+m
print(n,e,m,t) #, 同時輸出多個變數

#練習輸出平均值
a=t/2
print("平均:",a)

#另一種輸出字串格式化的方法
print(f"名字:{n} 英文成績:{e} 數學成績:{m}") #f 可以一次打一串

print("----------------------------")



#載入內建程式 math
import math
print(math.pi)
#設定小數第一位
print(f"The value of pi is approximately {a:.1f}")
#設定小數第三位
print(f"The value of pi is approximately {a:.3f}")

