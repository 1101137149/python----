e=100
m=50

print("兩科皆60以上")
print(f"e{e} m{m}")
if e>=60 and m>=60:
    print("錄取")
else:
    print("未錄取")

print("-------------------")

print("其中一科60以上")
if e>=60 or m>=60:
    print("錄取")
else:
    print("未錄取")

