try:
    with open("b.txt") as f: #with open 簡化寫法 最後會自動close()
        print("開檔成功")
except FileNotFoundError:
        print("b.txt檔找不到")