class Student:
    def __init__(self, namn:str, age:int):
        # SKAPA ALLA PROPERTIES/Egenskaper/Variabler
        # som hör till ritningen
        self.Namn = namn
        self.__Age = age
        self.KursLista = []
            

stefan = Student("Stefan", -12)
print(stefan.Namn)
stefan.__Age = -12
print(stefan.__Age)
stefan.Age = -123
print(stefan.Age)






# age får ju inte vara -

# from dataclasses import dataclass

# @dataclass
# class StudentV1:
#     Namn: str
#     PersonNummer:str
#     Kurser: list

# stefan = StudentV1("Stefan", "197208030000",[])
# josefine = StudentV1("J", 123,[])
