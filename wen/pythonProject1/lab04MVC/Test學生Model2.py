from lab04MVC.model import Date, Student

d=Date()
d.set(2022,7,11)

st1=Student()
st1.set(1,"Wen",d)
print(st1)

st2=Student()
st2.set(1,"Amy",d)
print(st2)

print("--修改日期--")
d.set(1999,1,23)
st1.set(1,"Wen",d)
print(st1)
print(st2)