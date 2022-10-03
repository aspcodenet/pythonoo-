class Person:
    def __init__(self, personNummer:str):
        self.__Namn = ""
        self.__PersonNummer = personNummer
    def SetPersonNummer(self, nytt:str):
        self.__PersonNummer = nytt
    def SetNamn(self, nytt:str):
        self.__Namn = nytt

s = Person("111122-1123")





class Ritning:
    def __init__(self):
        self.__Color = ""
    def Repaint(self, color:str):
        self.__Color = color
    def GetColor(self):
        return self.__Color


stefansHus = Ritning()        
stefansHus.Repaint("White")
annasHus = Ritning()       
annasHus.Repaint("Blue")
print(stefansHus.GetColor()) 
print(annasHus.GetColor()) 


# 1. class NAMN
# 2. def __init__(self)
#       här *skapar* du properties för objektet
# 3. __ på alla properties
# 4. getter och setters med VALIDERING
# 5. constructor - vad skicka in

class Student:
    def __init__(self, namn:str, age:int):
        # SKAPA ALLA PROPERTIES/Egenskaper/Variabler
        # som hör till ritningen
        self.__Namn = namn
        self.__Age = 0
        self.SetAge(age)
        self.__Antal = 0
        self.__Postnr = ""
        self.__KursLista = []
    
    def SetAge(self, newAge:int):
        if newAge > 0:
            self.__Age = newAge
    def GetAge(self):
        return self.__Age

stefan = Student("Stefan", -12)
stefan.SetAge(-12)
stefan.SetAge(132)
print(stefan.GetAge())






# age får ju inte vara -

# from dataclasses import dataclass

# @dataclass
# class StudentV1:
#     Namn: str
#     PersonNummer:str
#     Kurser: list

# stefan = StudentV1("Stefan", "197208030000",[])
# josefine = StudentV1("J", 123,[])
