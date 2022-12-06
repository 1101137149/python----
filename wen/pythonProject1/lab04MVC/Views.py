class OutputView:
    def __init__(self):
        self.st=None


    def set(self, st):
        self.st=st

    def output(self):
        print(self.st.id)
        print(self.st.name)
        print(self.st.birthdate)