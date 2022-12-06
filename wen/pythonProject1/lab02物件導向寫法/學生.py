#設計類別(將函數&變數打包) 命名慣例 第一個字大寫!
class Student:
    def __init__(self):
        self.name=None
        self.eng=0
        self.math=0

    def 修改值(self,name=None,eng=0,math=0):
        self.name=name
        self.eng = eng
        self.math = math

    def 總分(self):
        return self.eng+self.math

    def 顯示(self):
        tot=self.總分()
        print(self.name,self.eng,self.math)

#
# def 設定初值(st)
#     name=None
#     eng=None
#     st[0]=name
#     st[1]=eng
#
# st1=list()
# st2=list()
# 設定初值(st1)
# 設定初值(st2)


