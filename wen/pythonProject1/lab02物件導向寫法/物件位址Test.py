from lab02物件導向寫法.日期 import Date

#建立物件 由d1(記住位址)參考到物件資料的位址
d1=Date()
d1.修改值(2022,1,1)
d1.顯示()

#建立物件 由d2(記住位址)參考到物件資料的位址
d2=Date()
d2.修改值(2022,2,1)
d2.顯示()
print("----------------------------")
#id()取得物件位址
print('d1',id(d1))
print('d2',id(d2))

print("-----------d2=d1------------")
d2=d1
print('d1',id(d1))
print('d2',id(d2))
print("-----------d2.修改值(2033,3,3)------------")
d2.修改值(2033,3,3)
d2.顯示()
print("---------d1與d2參考相同物件 原d2物件成為垃圾---------------")
d1.顯示()
d2.顯示()
