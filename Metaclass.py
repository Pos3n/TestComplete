

class Student:
    
    def __init__(self, name, lastname, birthday):
        self._name = name
        self._lname = lastname
        self._birthday = birthday
    
    def __setattr__(self, obj, value):
        self.__dict__["_"+obj] = value

    def __getattr__(self, obj):
        return getattr(self,"_"+obj)

    


if __name__ == "__main__":
    s= Student("luca","Colacioppo", "13/07/1994")
    s.name="Daniele"
    print(s.name)




