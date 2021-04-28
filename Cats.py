class Cats:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def getName(self):
        return self.name

    def getSex(self):
        return self.sex

    def getAge(self):
        return self.age

    def getList(self):
        print(f'Кличка - {self.name}')
        print(f"Пол - {self.sex}")
        print(f"Возраст - {self.age}")
