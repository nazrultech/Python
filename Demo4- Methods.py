# class Stud:

#     college_name="ABC College"
  
#     #parameterizd constructor
#     def __init__(self, name, marks):
#         self.name= name  
#         self.marks= marks

#     def welcome(self):
#         print("Welcome student ", self.name)

#     def get_maks(self):
#         return self.marks

# s1 = Stud("Karan", 60) 
# print(s1.name , s1.marks) #Karan
# s1.welcome()
# print(s1.get_maks())

# ----

#lets practice
# Create Student class that takes name and marks of 3 subjects as argument in constructor .
# Then create a method to print the 

class Student:

    #parameterizd constructor
    def __init__(self, name, marks):
        self.name= name  
        self.marks= marks

    def get_Avg(self):
        sum=0
        for val in self.marks:
            sum +=val 
        print("Hi " , self.name, "your avg score is :", sum/3) 
        
s1 = Student("Nazrul, ", [75, 82, 98] ) 
s1.get_Avg()

s1.name= 'Nihal'
s1.get_Avg()
