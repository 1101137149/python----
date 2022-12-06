lottl=[33,10,15,21,28,30]

#"w"自動建立檔案，檔案若存在會覆蓋
with open("e.txt","w") as f:
    for 號碼 in lottl:
        字串=str(號碼) # str()數字轉字串
        # 字串=字串+"\n"
        字串+="\n" #字串寫入檔案最後包含Enter(換行)
        f.write(字串)