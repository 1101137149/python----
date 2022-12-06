def myfunc():
    x=200
    print(f"函數內區域變數x={x}")

def myfunc2():
    global x,y
    x=1
    y=2
    print(f"函數內global變數x={x}")
    print(f"函數內global變數y={y}")

    #主程式
x=300 #全域變數(global)
y=400 #全域變數(global)

print(f"主程式 全域變數 x={x}")
print(f"主程式 全域變數 y={y}")
print(f"--------------------")
myfunc()
print(f"主程式 全域變數 x={x}")
print(f"主程式 全域變數 y={y}")
print(f"--------------------")
myfunc2()
print(f"主程式 全域變數 x={x}")
print(f"主程式 全域變數 y={y}")
print(f"--------------------")





#自我挑戰
#將重複的部分簡化成函數呼叫
def fun():
    x = list()
    for n in range(1, 43):
        x.append(n)
    print(x)

x=fun()
#for n in range(1,43):
#    x.append(n)
print(x)

y=fun()
#for n in range(1,43):
#    y.append(n)
print(y)


print(f"--------------------")
#自我挑戰 設計函數 產生指定的豎立號碼
def 產生號碼(y):
    x=list()

    for n in range(1,y+1):
        x.append(n)
    return x



print(產生號碼(100))