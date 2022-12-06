a=input("name:")
b=input("name:")
c=input("name:")

print(id(a))
print(id(b))
print(id(c))

print("--------------")

#相同名稱位址會一樣 (變數設定一樣 電腦會自動使用同一份位址)
a="tom"
b="tony"
c="tom"

print(id(a))
print(id(b))
print(id(c))

