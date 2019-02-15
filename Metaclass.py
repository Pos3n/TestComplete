
class Person:
    
    def __init__(self, name, lastname, birthday):
        self.name = name
        self.lastname = lastname
        self.birthday = birthday
    
    def __setattr__(self, obj, value):
        self.__dict__[obj] = value
        

    def __getattr__(self, obj):
        return getattr(self, obj)

    def __repr__(self):
        return str("Nome: "+self.name+ "\nCognome: "+self.lastname+"\nData di nascita: "+self.birthday)

class Student(Person):

    def __init__(self):
        self._dict={}


if __name__ == "__main__":
    p = Person("luca","Colacioppo", "13/07/1994")
    print(p)
    i1 = str(input("inserisci un nome diverso: "))
    p.name = i1
    print(p)

