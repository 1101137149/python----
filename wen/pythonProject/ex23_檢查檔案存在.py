import os
if os.path.exists("C.txt"): #檢查檔案是否存在，避免發生錯誤
    with open("c.txt") as f:
        print("開檔成功")
    print("關檔成功")
else:
    print("c.txt檔找不到")