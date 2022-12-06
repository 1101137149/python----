def 輸入英文成績():
    #區域變數(變數在函式裡面)
    while True:
        try:
            #可能發生錯誤的程式
            x=float(input("請輸入英文成績:"))
            print("輸入完成")
            break
        except ValueError: #指名處理的錯誤型態(好寫法)
            print("格式錯誤 請輸入0-100")
    return x #返回結果

def 輸入數學成績():
    #區域變數(變數在函式裡面)
    while True:
        try:
            #可能發生錯誤的程式
            x=float(input("請輸入數學成績:"))
            print("輸入完成")
            break
        except ValueError: #指名處理的錯誤型態(好寫法)
            print("格式錯誤 請輸入0-100")
    return x #返回結果


#合併成一個函式
def 輸入科目成績(name):
    # 區域變數(變數在函式裡面)
    while True:
        try:
            # 可能發生錯誤的程式
            x = float(input(f"請輸入{name}成績:"))
            print("輸入完成")
            break
        except ValueError:  # 指名處理的錯誤型態(好寫法)
            print("格式錯誤 請輸入0-100")
    return x  # 返回結果

#主程式
#全域變數(變數在函式外面)
e=輸入英文成績()
print(f"結果{e}")

m=輸入數學成績()
print(f"結果{m}")


a=輸入科目成績("國文")
print(f"結果{a}")
b=輸入科目成績("自然")
print(f"結果{b}")