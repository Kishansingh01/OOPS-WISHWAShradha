# class Student:
#     name="Kishan"
#     class1 = "BSc from computer science and AI"
# s1 = Student()
# print(s1.name)
# print(s1.class1)
# s2=Student ()
# print(s2)
# print(s2.class1)

# class Car:
#     color="White"
#     Brand_Name="Mercedes"
#     Price=50000000
# R1=Car()
# print(R1.color)
# print(R1.Brand_Name) 
# print(R1.Price) 

# class Student:
#     name="Kishan"
#     def __init__(self):
#         print("Adding new students from Database")
# s1 = Student()
# print(s1)
       
# class Student:
#     def __init__(self,FullName):
#         self.FullName=FullName
# s1=Student("Kishan")
# print(s1.FullName)

# class State:
#     def __init__(self,statename,location):
#         self.state =statename
#         self.locate =location
#         print("Adding new state")
# s1=State("Bihar","Northern")   
# print(s1.state)  
# print(s1.locate)
# s2=State("Punjab","Western") 
# print(s2.state) 
# print(s2.locate)
# print(s2.state,s2.locate)

# class Student:
#     def __init__(self):
#         pass
#     def __init__(self,name,enrollment):
#         self.name=name
#         self.enrollment=enrollment
#         print("i am also here")
# s1=Student("Kishan","2301010056") 
# print(s1.name,s1.enrollment)       
#Apne Jarurat ke anusaar hm self lete hai aur banate hai:

# class Student:
#     def __init__(self,name,rollno):
#         self.name=name
#         self.rollno=rollno
#         print("Hello friends")


class Student:
    def __init__(self,Name,RollNo,Class):
        self.Name=Name
        self.RollNo=RollNo
        self.Class=Class
s1=Student("Kishan Kumar","2301010056","BS(Honors)") 
print(s1.Name)     
print(s1.RollNo) 
print(s1.Class)        