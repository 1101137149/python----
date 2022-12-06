n=input("輸入姓名:")
print(f"歡迎光臨{n}")
print("歡迎光臨",n)

e=input("輸入英文成績:")
m=input("輸入數學成績:")

print(f"type e={type(e)}")
print(f"type m={type(m)}")
t=e+m
print(f"總分{t}")
print("----------float-----------")


e=float(input("輸入英文成績:"))
m=float(input("輸入數學成績:"))

print(f"type e={type(e)}")
print(f"type m={type(m)}")
t=e+m
print(f"總分{t}")
