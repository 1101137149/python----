from lab04MVC.PyWeb作業01_Controller import Controller


class OutputView:
    def __init__(self):
        self.st=None


    def set(self, st):
        self.st=st

    def output(self):
        # print(self.st.id)
        # print(self.st.name)
        # print(self.st.price)
        c = Controller()
        c.run()


v=OutputView()
v.output()