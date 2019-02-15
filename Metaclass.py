import functools

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

    def __init__(self, name, lastname, birthday, esamivoti = {} ):
        super().__init__(name, lastname, birthday)
        self.exam={}
        self.exam.update(esamivoti)


    def __repr__(self):
        return str("Nome: "+self.name+ "\nCognome: "+\
            self.lastname+"\nData di nascita: "+self.birthday+\
            "\nExams: \n"+str(list(self.exam.items())))

    @property    
    def get_avarage(self):
        tipo = list(self.exam.values())
        return functools.reduce(lambda x,y: x+y, tipo)/len(tipo)


if __name__ == "__main__":
    p = Student("luca","Colacioppo", "13/07/1994",{"matematica":20})
    p.exam.update({"GeoStoria": 27})
    print(p)
    print(p.get_avarage)



    #i1 = str(input("inserisci un nome diverso: "))
    #p.name = i1
    #print(p)   