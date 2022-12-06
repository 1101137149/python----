with open("f.txt") as f:
    for 行 in f:
        #\n Enter 換行符號
        #行 是從檔案獨到的一行字串 字串有replace()取代功能
        行=行.replace("\n","-") #璇找Enter取代成 沒有字(刪除)
        print(行)