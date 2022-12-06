from Lab07序列化.DemoSerializer import Product


class Serializer:
    def __init__(self):
        pass

    def serialize(self,all):
        p1 = Product(1, "Apple", 100)
        p2 = Product(2, "Banana", 200)
        all = [p1, p2]
        data = list()
        for p in all:
            d = {'id': p.id, 'name': p.name, 'price': p.price}
            data.append(d)

        import json
        s = json.dumps(data)
        return s
