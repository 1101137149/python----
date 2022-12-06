from lab05MVC.零件 import A,B,C


class 整合:
    def __init__(self):
        pass

    def run(self):
        a=A()
        a.set(100)


        b=B()
        b.set()

        c=C()
        c.set(b)
        c.do_something()