class Product:
    def __init__(self,id,name,price): #建構子
        self.id=id;
        self.name=name;
        self.price=price;

    def __str__(self): #建構子
        return f"{self.id}-{self.name}-{self.price}"