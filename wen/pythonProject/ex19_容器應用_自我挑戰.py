a = dict()
def myfun(num,data):
    f = ["新增", "修改", "查詢", "刪除"]
    k = input(f"請輸入需{f[num-1]}的郵遞區號=")
    if k in data:
        if num==3 :
            print(f"查詢成功!a={data[k]}")
        elif num==4:
            del a[k]
        else:
            name = input(f"請輸入需{f[num-1]}的區域名稱=")
            data[k] = name
        print(f"{f[num-1]}成功!a={data}")
    else:
        print(f"此郵遞區號不存在無法{f[num-1]}!")
        print(f"目前資料={data}")

while True:

    print("請輸入數字 1=新增 2=修改 3=查詢 4=刪除")
    select=input("數字=")
    if select=="1":

        print(f"目前資料={a}")

        key = input("請輸入需新增的郵遞區號=")
        #判斷是否有重複的，沒有才可新增
        if key not in a:
            name = input("請輸入需新增的區域名稱=")
            a[key] = name
            print(f"新增成功!a={a}")
        else:
            print("此郵遞區號已存在無法新增!")
            print(f"目前資料={a}")
    elif select=="2":
        print(f"目前資料={a}")

        myfun(2,a)

        # if key in a:
        #     name = input("請輸入需修改的區域名稱=")
        #     a[key] = name
        #     print(f"修改成功!a={a}")
        # else:
        #     print("此郵遞區號不存在無法修改!")
        #     print(f"目前資料={a}")
    elif select=="3":
        myfun(3, a)

        # print(f"目前資料={a}")
        # key = input("請輸入需查詢的郵遞區號=")
        # if key in a:
        #     print(f"查詢成功!a={a[key]}")
        # else:
        #     print("此郵遞區號不存在無法查詢!")
        #     print(f"目前資料={a}")
    elif select=="4":
        myfun(4, a)
        # print(f"目前資料={a}")
        # key = input("請輸入需刪除的郵遞區號=")
        # if key in a:
        #     del a[key]
        #     print(f"刪除成功!a={a}")
        # else:
        #     print("此郵遞區號不存在無法刪除!")
        #     print(f"目前資料={a}")
    else:
        print(f"結束功能!")
        break


