from lab04MVC.model import Date

d=Date()
print(d) #如果類別有 __str__會自動呼叫
d.set(2022,7,11)
print(d) #如果類別有 __str__會自動呼叫

