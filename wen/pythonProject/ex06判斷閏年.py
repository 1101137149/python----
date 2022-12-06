
y=2016
print(y/4)
#print(f"餘數{y%4}") #除錯用

四倍數=y%4==0
#print(f"四倍數{四倍數}") #除錯用

非百倍數=not(y%100==0)
#print(f"非百倍數{非百倍數}") #除錯用

四百倍數=y%400==0
#print(f"四百倍數{四百倍數}") #除錯用

if 四倍數:
    print(f"{y}是4的倍數")

閏年1=四倍數 and 非百倍數
閏年2=四百倍數

if 閏年1 or 閏年2:
    print(f"{y}是閏年")
else:
    print(f"{y}不是閏年")

print("-----------------")


#函數寫法 def
#函數盡量邏輯簡單
def 是閏年(year):
    四倍數=(year % 4)==0
    百倍數=(year % 100)==0
    四百倍數=(year % 400)==0
    閏年條件1= 四倍數 and (not 百倍數)
    閏年條件2= 四百倍數
    if 閏年條件1 or 閏年條件2:
        return True
    else:
        return False

print(是閏年(1979))
print(是閏年(1980))
print(是閏年(1900))
print(是閏年(2000))