class Pet:

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def getName(self):
        return self.name

    def getGender(self):
        return self.gender

    def getEge(self):
        return self.age

    def output_info_pet(self):
        print(f'Имя животного: {self.name},\n Пол животного: {self.gender},\n Возраст животного: {self.age}')

