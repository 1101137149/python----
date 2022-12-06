from lab04MVC.model import Date, Student

d=Date()
d.set(2000,1,1)



st=Student()
st.set(1,"Wen",d)
print(st)