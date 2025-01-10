# class Stud:
#     def __init__(self):
#         print("Calling constructor when object s1 called")
# s1 = Stud() 
# -----

# class Stud:
#     def __init__(self):
#         print(self) #<__main__.Stud object at 0x000001387E066A50>
#         print("Calling constructor when object s1 called")
# s1 = Stud() 
# print(s1) #<__main__.Stud object at 0x000001387E066A50>

# ----------

# class Stud:
#     def __init__(self, fullname):
#         self.name= fullname
#         print("Calling constructor when object s1 called")

# s1 = Stud("Karan") 
# print(s1.name) #Karan

# -------


# class Stud:
#     def __init__(self, fullname):
#         self.name= fullname
#         print("Calling constructor when object called")

# s1 = Stud("Karan") 
# print(s1.name) #Karan

# s2=Stud("Arjun")
# print(s2.name) # Arjun

# -----

# class Stud:
#     def __init__(self, fullname):
#         self.name= fullname
#         print("Calling constructor when object called " + fullname)

# s1 = Stud("Karan") 
# print(s1.name) #Karan

# s2=Stud("Arjun")
# print(s2.name) # Arjun


# -----

# Awlways use same name


# class Stud:
#     def __init__(self, name, marks):
#         self.name= name
#         self.marks= marks
#         print("Calling constructor when object called")

# s1 = Stud("Karan", 60) 
# print(s1.name , s1.marks) #Karan

# s2=Stud("Arjun", 80)
# print(s2.name, s2.marks) # Arjun

# -----


class Stud:
    #default constructor
    def __init__(self):
        pass

    #parameterizd constructor
    def __init__(self, name, marks):
        self.name= name
        self.marks= marks
        print("Calling constructor when object called")

s1 = Stud("Karan", 60) 
print(s1.name , s1.marks) #Karan

s2=Stud("Arjun", 80)
print(s2.name, s2.marks) # Arjun