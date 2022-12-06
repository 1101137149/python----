class Date:
    def __init__(self):
        self.year=None
        self.month=None
        self.day=None

    def 顯示(self):
        print(self.year,self.month,self.day)

    def 修改值(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day