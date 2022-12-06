#t文字檔
#f=open("a.txt","rt") #預設為rt 即 開文字檔讀資料
#可能發生FileNotFoundError 檔案找不到

f=None
try:
    #開檔可能失敗 f區域變數(local variable)必須先設定值
    f=open("a.txt")
    print('開檔成功')
except FileNotFoundError:
    print('a.txt檔找不到')
finally:
    if f is not None:
        f.close()
        print('關檔成功')
