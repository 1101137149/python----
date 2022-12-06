try:
    #可能發生錯誤的程式
    e=float(input("請輸入英文成績:"))
    print("輸入完成")
except ValueError: #好的寫法 指名處理的錯誤類型
    print("格式錯誤,請輸入0-100")
except: #壞的寫法 不指名錯誤類型
    #處理其他錯誤
    print("不知名錯誤")
finally:
    print("結束")

while True:
    try:
        m=float(input("請輸入數學成績:"))
        if m<0 or m>100:
            print("請輸入0-100")
        else:
            break
    except:
        print("格式錯誤,請輸入0-100")
print("輸入完成")
