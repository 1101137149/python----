from lab04MVC.Views import OutputView
from lab04MVC.model import Date,Student

#準備零件
d=Date()
d.set(2000,1,1)

#準備零件
st1=Student()
st1.set(1,"Tom",d)

#準備零件
ov=OutputView()
ov.set(st1)
ov.output()