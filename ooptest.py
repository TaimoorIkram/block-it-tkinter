from os import name
from random import choice, randint


class Student():
    total=0
    def __init__(self,name:str,surname:str,school:str,hostel:str,age:int) -> None:
        self.name=name
        self.surname=surname
        self.school=school
        self.hostel=hostel
        self.total+=1
        self.age=age
    def __str__(self) -> str:
        hostelite = "non-hostelite" if self.hostel=='none' else "Hostelite"
        return self.name+" "+self.surname+" is a "+hostelite+" and belongs to school "+self.school
    def getname(self):
        return self.name+" "+self.surname
    def totalstudents(self):
        return self.total
    def gethostel(self):
        return "Non-Hostelite" if self.hostel=="none" else self.hostel
    def misguide(self,miguider,info:str):
        if info.upper=='TOTAL':
            self.total*=randint([1,2,3,4])
    def checkcorrectness(self):
        return f"{self.name} has been misguided." if self.totalstudents!=Student.totalstudents else f'{self.name} hasn\'t been misguided.'
    def __add__(self,other):
        return f"{self.name} weds {other.name}? WTF bro."
    def __lt__(self,other):
        if self.age<other.age:
            return f"{self.name} is younger than {other.name} by {other.age-self.age} years!"
        elif self.age>other.age:
            return f"{other.name} is younger than {self.name} by {self.age-other.age} years!"
    def askname(self,other):
        return f'Their name is {other.name}.'
    
    @classmethod
    def fromfullname(clas,name:str,school:str,hostel:str,age:int):
        fore,sur=name.split()
        school=school
        hostel=hostel
        age=age
        return Student(fore,sur,school,hostel,age)
    
    @staticmethod
    def getgrade(marks,subject):
        grade='F'
        if marks>80:grade="A"
        elif marks>60:grade="B"
        elif marks>40:grade="C"
        elif marks>20:grade="D"
        return f'You scored {grade} in {subject}.'
s1=Student("Asif","Jamil","SEECS","none",19)
s2=Student("Alia","Ashraf","SMME","Ayesha Block",20)
s3=Student.fromfullname("Aleeza Ashraf","SMME","Ayesha Block",15)

s1.misguide(s2,"total")
print(s2.getgrade(45,"Calculus"))
print(s1.checkcorrectness())