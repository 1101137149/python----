from Lab07序列化.DemoSerializer import Product
from Lab07序列化.serializers import Serializer

p1=Product(1,"Apple",100)
Product.object.save(p1)

p2=Product(2,"Banana",200)
Product.object.save(p2)


ser=Serializer()
s=ser.serialize(Product.object.all())
print(s)
