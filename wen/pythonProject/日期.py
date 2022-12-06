import random



#判斷閏年函數
def 閏年判斷(year):
    四倍數 =year %4==0
    百倍數 =year %100==0
    四百倍數=year %400==0
    閏年條件1 = 四倍數 and (not 百倍數)
    閏年條件2 = 四百倍數
    if 閏年條件1 or 閏年條件2:
        return True
    else:
        return False



#判斷日期天數函數
def 日期判斷(m):
    if 閏年判斷(y) and m == 2:
        return 29
    elif m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        return 31
    elif m == 4 or m == 6 or m == 9 or m == 11:
        return 30
    else:
        return 28



#主程式
#用亂數產生日期 年月日
#必須是合理的日期 例如2月 最多28或29天 要判斷閏年

#亂數產生年
y=random.randint(2000,2500)
#print(y)


#亂數產生月
m=random.randint(1,12)
#print(m)


#亂數產生日
dnum=日期判斷(m)
#print(dnum)
d=random.randint(1,dnum)
#print(d)


print(f"{y}/{m}/{d}")