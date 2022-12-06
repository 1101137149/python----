class OutputView:
    def __init__(self):
        self.product=None


    def set(self, product):
        self.product=product

    def output(self):
        print(self.product)
