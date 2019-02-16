import functools
import datetime

class Person:
    
    def __init__(self, name, lastname, birthday):
        self._name = name
        self._lastname = lastname
        self._birthday = birthday
    
    def __setattr__(self, obj, value):
        self.__dict__["____"+obj] = value
        
    def __getattr__(self, obj):
        return getattr(self,"_"+obj)

    def __repr__(self):
        return str("Nome: "+self._name+ "\nCognome: "+self._lastname+"\nData di nascita: "+self._birthday)



class Student(Person):

    def __init__(self, name, lastname, birthday, esamivoti = {} ):
        super().__init__(name, lastname, birthday)
        self._exam={}
        self._exam.update(esamivoti)

    def __repr__(self):
        return str("Nome: "+self._name+ "\nCognome: "+\
            self._lastname+"\nData di nascita: "+self._birthday+\
            "\nExams: "+str(list(self._exam.items())))

    @property    
    def get_avarage(self):
        tipo = list(self._exam.values())
        return functools.reduce(lambda x,y: x+y, tipo)/len(tipo)

class Worker(Person):
    def __init__(self, name, lastname, birthday, pay_per_hour):
        super().__init__(name, lastname, birthday)
        self._pay = pay_per_hour

    @property
    def day_salary(self):
        print("Considering 8 working hours a day")
        return self._pay*8
    
    @property
    def week_salary(self):
        print("Considering 5 working days a week")
        return self._pay*5*8
    
    @property
    def year_salary(self):
        print("Considering 12 working week a year")
        return self._pay*5*8*12

class Wizard(Person):
    def __init__(self, name, lastname, birthday):
        super().__init__(name, lastname, birthday)
        self._current_date=(str(datetime.datetime.now().year)) 

       
    def get_age(self):
        return int(self._current_date)-int(self._birthday[6:])

    def set_age(self, value):
        print("Setting age")
        self._birthday = value
        
    age = property(fget=get_age, fset=set_age)


if __name__ == "__main__":
    s = Student("Luca","Colacioppo", "13/07/1994",{"matematica":20})
    s.exam.update({"GeoStoria": 27})
    print("Student test")
    print(s)
    print("Avarage is: " + str(s.get_avarage))
    print("Worker test")
    w = Worker("Matteo","Colacioppo", "13/07/1994",10)
    print("Worker test")
    print(w)
    w.pay = 20
    print("Day salary: " + str(w.day_salary))
    print("Week salary: " + str(w.week_salary))
    print("Year salary: " + str(w.year_salary))
    v = Wizard("Giovanni","Colacioppo", "13/07/1994")
    print(v)
    print(v.age)
    v.set_age("13/07/2010") 
    print(v.age)
