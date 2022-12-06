fruits=["apple","banana","cherry"]
print(fruits)
if "banana" in fruits:
    print("yes")

#s如果不在fruits當中才加入，避免加入入重複資料
s="aaa"
if s not in fruits:
    fruits.append(s)

print(fruits)