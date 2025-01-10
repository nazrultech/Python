class Student:

    #parameterizd constructor
    def __init__(self, name, marks):
        self.name= name  
        self.marks= marks
    
    #Static method
    @staticmethod
    def hello():
        print("hello")

    def get_Avg(self):
        sum=0
        for val in self.marks:
            sum +=val 
        print("Hi " , self.name, "your avg score is :", sum/3) 
        
s1 = Student("Nazrul, ", [75, 82, 98] ) 
s1.get_Avg()

s1.name= 'Nihal'
s1.get_Avg()
s1.hello()
