#客戶名稱
def CNameTxT():

    while True:
        name=input("請輸入客戶名稱:")
        if len(name)<2:
            print("輸入錯誤，請至少輸入兩個字的名稱")
        else:
            break
    return name

#樂透號碼
def lottoTxT():

    lotto=set()
    checkLen=1
    while True:
        try:
            lottoLen=len(lotto)+1
            num=input(f"請輸入第{lottoLen}個樂透號碼(共六碼):")

            #判斷是否為數字1~42
            if int(num)<=42 and int(num)>=1:
                lotto.add(num)
                checkLen =checkLen+1
                #確認長度判斷是否輸入了重複號碼
                if checkLen!=len(lotto)+1:
                    print("輸入了重複的號碼，請重新輸入")
                    checkLen = checkLen - 1
                elif checkLen==len(lotto)+1 and len(lotto) < 6:
                    print(f"已存入第{lottoLen}個號碼")
                else:
                    break
            else:
                print("請輸入1~42之間的數字")
        except ValueError:
            print("格式錯誤,請輸入1~42之間的數字")
    return lotto

    # print(lotto)

#建立文字檔將資料存入
def dataToFile(type,dictdata): #type w=自動建立檔案，檔案若存在會覆蓋 a=自動建立檔案，檔案若存在，附加資料不覆蓋
    with open("Lotto.txt",type,encoding="UTF-8") as f:  #"w"自動建立檔案，檔案若存在會覆蓋
        txtStr=""
        for k,v in dictdata.items():
            f.write(str(k)+"-"+str(v)+"\n")

        # for x in dictdata:
        #     print(str(x))
        #     print(dictdata[x])
        #     txtStr +=str(x) + str(dictdata[x])+"\n"
        #     # txtStr+="名稱="+str(x)+" "
        #     # txtStr += "樂透號碼=" + str(dictdata[x])+"\n"
        #     txtStr += "\n----------\n"
        # f.write(txtStr)

#讀取檔案放到字典
def readFile():
    d = {}
    with open("Lotto.txt") as f:
        for line in f.readlines():
            # line=line.strip()
            line=line.replace("{","")
            line=line.replace("}","")
            line=line.replace("'","")
            line=line.replace("\n","")
            line=line.replace(" ","")


            # print(line)
            k=line.split('-')[0]
            # print(k)
            v=line.split('-')[1].split(",")
            # print(v)
            d[k]=v
            # (key, val) = line.split()
            # d[int(key)] = val
    return d
        # for k,v in f:
        #
        #     row = row.replace("\n", "")  # 將\n取代為空白
        #     print(row)




#主程式
#使用input 輸入 客戶名稱+樂透號碼
#客戶名稱長度至少2個字、樂透號碼不能重複
#儲存文字檔 客戶名稱、6個樂透號碼

Cname=CNameTxT()
Clotto=lottoTxT()
#寫入dict紀錄
data=dict()
data[Cname]=Clotto
#建立文字檔將資料存入
dataToFile("w",data)



#進階挑戰1
#連續輸入3筆資料(客戶名稱、樂透號碼)
#客戶名稱不能重複
#使用附加模式寫入3筆資料 要包含上述練習的第一筆資料

print("--進階挑戰1--")

data2 = dict()

#連續輸入3次資料
while True:
    #確認客戶名稱
    while True:
        Cname = CNameTxT()
        if Cname not in data2:
            break
        else:
            print("該客戶名稱已存在，請重新輸入!")
    #樂透
    Clotto =lottoTxT()

    # 將這次資料寫入dict紀錄
    data2[Cname] = Clotto
    if len(data2)==3:
        break
print(data2)
#建立文字檔將資料存入
dataToFile("a",data2)


#進階挑戰2
#讀取文字檔裡的4筆資料
#將4筆資料放入dict()
#透過客戶名稱查詢樂透號碼

print("--進階挑戰2--")

print(readFile())

#寫入字典
filedata=readFile()

#輸入客戶名稱查詢樂透號碼
while True:
    n=input("請輸入客戶名稱來查詢樂透號碼:")
    
    if n in filedata:
        print(filedata[n])
        break
    else:
        print("查無此客戶，請重新輸入！")


#進階挑戰3
#修改客戶名稱
#選項1:修改名字
#選項2:修改樂透號碼(重產生一組)
#修改資料後，儲存文字檔
print("--進階挑戰3--")

while True:
    print("請輸入數字來修改客戶資料 1=修改名字 2=修改樂透號碼")
    select=input("數字=")
    if select=="1":
        # print(f"目前資料={filedata}")
        # myfun(1, filedata)
        key = input("請輸入要修改名字的舊名字=")
        #判斷有無資料 有資料才能修改
        if key in filedata:
            name = input("請輸入需修改的新名字=")
            filedata[name] = filedata.pop(key)
            #依照新的dict 去覆蓋整個檔案
            dataToFile("w", filedata)
            break
        else:
            print("此名字不存在無法修改!")
    elif select=="2":
        key = input("請輸入要修改樂透的名字=")
        if key in filedata:
            newlotto = lottoTxT()
            filedata[key]=newlotto
            # 依照新的dict 去覆蓋整個檔案
            dataToFile("w", filedata)
            break
        else:
            print("此名字不存在無法修改樂透!")
    else:
        print(f"輸入錯誤請重新再試!!")

print(f"目前資料={filedata}")