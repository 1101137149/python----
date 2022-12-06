#建立list簡化寫法[]
a = ["apple" , "banana" , "cherry" , "apple"]
print(a)
print(a[0])
print(a[1])
print(f'list長度(項目數量) {len(a)}')
print(f'apple長度(字數) {len(a[0])}')

print("-------------------------------")

#建立list 可接受任意類型資料
b=[100,3.14,"Hello"]
print(b)
print(b[0])
print(b[1])
print(f'b 長度 {len(b)}')
print(type(a))
print(type(b))

print("-------------------------------")

#標準寫法 透過list() 建立list
c=list(("a","b","c"))  #list裡面要在包一個括號放自己的列表
print(c)
c.append("d")
print(c)
c.insert(1,"x") #插入第1項
print(c)
c.remove("a") #刪除 指定資料
print(c)
c.pop(0) #刪除 指定項目 需要索引編號
print(c)
