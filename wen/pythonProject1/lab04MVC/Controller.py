from lab04MVC.Views import OutputView
from lab04MVC.model import Date,Student


class Controller:
    def __init__(self):
        pass

    def run(self):
        #準備零件
        d=Date()
        d.set(2000,1,1)

        #準備零件
        st1=Student()
        st1.set(1,"Tom",d)

        ov = OutputView()
        ov.set(st1)
        ov.output()