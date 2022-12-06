filename=r"C:\Users\user\Desktop\學生.txt"

#無論讀寫 開啟檔案 皆指定採用萬國碼 UTF-8避免中文變亂碼
with open(filename,"w",encoding="UTF-8")as f:
    name="湯姆"
    eng=100
    math=99
    f.write(name)
    f.write("\n")
    #文字檔只能輸出字串
    f.write(str(eng)) #str()轉成字串
    f.write("\n")
    f.write(str(math)) #str()轉成字串
    f.write("\n")
