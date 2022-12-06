from lab05MVC.自我挑戰_models import Product
from lab05MVC.自我挑戰_views import OutputView


class Controller:
    def __init__(self):
        pass
    def run(self):
        product=Product()
        product.set(1,"apple",100)
        ov=OutputView()
        ov.set(product)
        ov.output()