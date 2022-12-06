a=["apple","banana","cherry"]
for x in a:
    print(x)

print(range(3)) #即range(0,3),範圍0~2 3不含
print(range(1,3)) #即range(1,3),範圍1~2 3不含

print(f"長度",len(a))
for i in range(len(a)):
    print(f"第{i}項")
    print(a[i])

for n in range(1,4): #4不含 ,1~3
    print(n)

b=list()
for n in range(1,4):#4不含 ,1~3
    b.append(n) #將n加入b
print("b",b)