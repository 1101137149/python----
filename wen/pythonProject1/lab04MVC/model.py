class Date:
    def __init__(self):
        self.year=None
        self.month=None
        self.day=None

    def set(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return f"{self.year}-{self.month}-{self.day}"

class Student:
    def __init__(self):
        self.id=None
        self.name=None
        self.birthdate=None

    def set(self,id,name,birthdate):
        self.id = id
        self.name = name
        # self.birthday =birthday

        self.birthdate = Date()
        self.birthdate.year=birthdate.year
        self.birthdate.month=birthdate.month
        self.birthdate.day=birthdate.day

    def __str__(self):
        return f"{self.id}-{self.name}-{self.birthdate}"


