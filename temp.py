class Person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age 

person1 = Person("rishabh",20)
print(person1.__name)
# dir(person1)