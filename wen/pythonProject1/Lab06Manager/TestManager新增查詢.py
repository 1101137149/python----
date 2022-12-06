#p1 & p2共享 objects
from Lab06Manager.models import Product

p1=Product(1,"Apple",100)
Product.object.save(p1)

p2=Product(2,"Banana",200)
Product.object.save(p2)


print("--查詢all--")
for p in Product.object.all():
    print(p)

print("--查詢id=1--")
print(Product.object.filter(id=1))