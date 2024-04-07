class Person:
    name='Joao Carlos'
    age = 16
    height = '1.89'
    hasMoustache = True
    useGlasses = True

    def setAge(self, age):
        self.age = age
    
    def setName(self, name):
        self.name = name

    def print_data(self):
        print('NAME: '+ self.name)
        print('AGE: ')
        print(self.age)
        print('HEIGHT: '+ self.height)
        print('HAS MOUSTACHE: ')
        print(self.hasMoustache)
        print('USE GLASSES: ')
        print(self.useGlasses)
    
    def getDriversLicense(self, age):
        if age >= 18:
            print('Congratulations! You can get your driver license')
        else:
            print('Sorry! You can not get your driver license')

class Child(Person):
    useDaiper = True

    def toEnterSchool(self):
        if(self.age >= 5):
            print('Congratulations! You can to enter in school')
        else:
            print('Sorry! You can not to enter in school')
        
person = Person()
child = Child()

person.print_data()
person.getDriversLicense(person.age)

child.setAge(4)
child.setName('Pedro Lucas')

child.print_data()
print('USE DAIPER: ')
print(child.useDaiper)

child.toEnterSchool()
