from rand import GetPassword
class Student:
    def __init__(self,name,lastname,birth,gender,mark,spec,number):
        if len(name)<26:
            self.__name=name
        else:
            raise ValueError("maximum 25 symbols")
        if len(name)<51:
            self.__lastname=lastname
        else:
            raise ValueError("maximum 50 symbols")
        self.__birth=birth
        if gender=='Male' or gender=='M':
            self.__gender=gender
        elif gender=='Female' or gender=='F':
            self.__gender=gender
        else:
            raise ValueError("only Male Female")    
        if mark>0 and mark<11:
            self.__mark=mark
        else:
            raise ValueError("from 0 to 10")
        if len(spec)<51:
                self.__spec=spec
        else:
            raise ValueError("maximum 50 symbols")
        if (float(number)==int(number)):
            self.__number=number
        else:
            raise ValueError("only int")
    def __getMark(self):
        return self.__mark
    def __setMark(self, m):
        if m>0 and m<11:
            self.__mark=m
        else:
            raise ValueError("from 0 to 10")
    def __getName(self):
        return self.__name
    def __getLastName(self):
        return self.__lastname
    def __getBirth(self):
        return self.__birth
    def __getGender(self):
        return self.__gender
    def __getSpec(self):
        return self.__spec
    def __setSpec(self, spec):
        if len(spec)<51:
                self.__spec=spec
        else:
            raise ValueError("maximum 50 symbols")
    def __getNumber(self):
        return self.__number
    def __setNumber(self, number):
        if (float(number)==int(number)):
            self.__number=number
        else:
            raise ValueError("only int")
    Name=property(__getName)
    LastName=property(__getLastName)
    Birth=property(__getBirth)
    Gender=property(__getGender)
    Mark=property(__getMark,__setMark)
    Spec=property(__getSpec,__setSpec)
    Number=property(__getNumber,__setNumber)
class Extended_Student(Student):
    def __init__(self, name, lastname,birth,gender,mark,spec,number):
        Student.__init__(self, name, lastname,birth,gender,mark,spec,number)
        self.Login=str(name[0])+lastname
        ps=GetPassword()
        self.Password=ps.GetInt()+ps.GetString()