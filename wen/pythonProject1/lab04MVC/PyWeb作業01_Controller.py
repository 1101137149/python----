from lab04MVC.PyWeb作業01_Model import Product
import csv
import json

class Controller:
    def __init__(self):
        pass




    def run(self):
        db = list()
        p1 = Product(1, "apple", 100)
        p2 = Product(2, "banana", 500)
        p3 = Product(3, "Cherry", 200)
        # 新增
        db = self.Insert(db,p1)
        db = self.Insert(db,p2)
        db = self.Insert(db,p3)

        # 查詢全部資料
        self.SelectAll(db)

        # 查詢某筆
        self.Select(db, 2)

        # 修改
        new_p1=Product(1, "New apple", 1000)
        db=self.Update(db, 1, new_p1)

        # 查詢全部資料
        self.SelectAll(db)


        #刪除
        # self.Delete(db,1)

        #查詢全部資料
        self.SelectAll(db)



        #進階挑戰1
        #增加存檔 & 讀檔 (.csv)
        self.listToCSV(db)
        self.readCSV()

        #進階挑戰2
        self.listToJSON(db)
        self.readJSON()


    # 新增
    def Insert(self,list,prodata):
        list.append(prodata)
        p=list[len(list)-1]
        print(f"--新增資料--\n{p}\n")
        return list

    # 查詢單一資料
    def Select(self,list, id):
        print(f"--查詢第{id}筆資料--\n{list[id - 1]}\n")
        # return list[id - 1]

    # 查詢資料
    def SelectAll(self,list):
        print(f"--查詢全部資料--")
        for p in list:
            print(p)

    # 修改
    def Update(self,list, id, newdata):
        Olddata = list[id - 1]

        list[id - 1] = newdata
        print(f"--修改第{id}筆成功--\n{list[id - 1]}\n")
        return list

    # 刪除
    def Delete(self,list, id):
        p = list[id - 1]
        if p is not None:
            list[id - 1] = None;
            print(f"--刪除第{id}筆成功--\n{list[id - 1]}\n")
            return list
        else:
            print(f"--刪除第{id}筆失敗，資料不存在--\n")
            return list

    #CSV寫入
    def listToCSV(self,list):
        print('--進階挑戰1-寫到CSV裡--')
        with open('作業01.csv', 'w', newline="",encoding="UTF-8") as f:
            # using csv.writer method from CSV package
            write = csv.writer(f)
            titles = ['編號', '產品', '價格']
            write.writerow(titles)
            for a in list:
                print(str(a).replace("-",",").split(","))
                write.writerow(str(a).replace("-",",").split(","))
            new=['4', 'Iphone', '5000']
            write.writerow(new)
            print(str(new))

    #CSV讀取
    def readCSV(self):
        print('--進階挑戰1-讀CSV資料--')
        with open('作業01.csv',encoding="utf-8") as f:
            reader = csv.reader(f)
            data = [tuple(row) for row in reader]

            print(data)


    #JSON寫入
    def listToJSON(self,list):
        print('--進階挑戰2-寫到JSON裡--')
        with open('作業01.json', 'w',encoding="UTF-8") as f:
            p=Product(4,'iphone',"5000")
            list=self.Insert(list,p)
            print(type(list))
            json.dump([a.__dict__ for a in list], f, ensure_ascii=False)

        for a in list:
            print(a.__dict__)


    #JSON讀取
    def readJSON(self):
        print('--進階挑戰2-讀JSON資料--')
        with open('作業01.json', encoding="utf-8") as f:
            data = json.load(f)
            print(data)




# c=Controller()
# c.run()


