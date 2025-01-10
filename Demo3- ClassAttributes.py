# class Stud:

#     college_name="ABC College"

#     #parameterizd constructor
#     def __init__(self, name, marks):
#         self.name= name
#         self.marks= marks
#         print("Calling constructor when object called")

# s1 = Stud("Karan", 60) 
# print(s1.name , s1.marks) #Karan

# s2=Stud("Arjun", 80)
# print(s2.name, s2.marks) # Arjun
# # print(s2.college_name) # ABC College #object.attribute
# print(Stud.college_name) # ABC College #Class.Attribute

# ----

class Stud:

    college_name="ABC College"
    name="Anonymous" # class attribute

    #parameterizd constructor
    def __init__(self, name, marks):
        self.name= name  # obj attribute > class attribute ; ojbj attribute has higher preference
        self.marks= marks
        print("Calling constructor when object called")

s1 = Stud("Karan", 60) 
print(s1.name , s1.marks) #Karan


