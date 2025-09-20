# 🔹 5. Student Grades

# Create a class Student with attributes name and a list of marks.

# Add a method average() to calculate the average mark.

# Add another method has_passed() that returns True if average ≥ 40.

class Student:
    def __init__(self,name:str,mark:float):
        self.name = name
        self.mark = mark
        
    def average(self):
        if not self.mark:
            return 0
        return sum(self.mark)/len(self.mark)
    
    def has_passed(self):
        return self.average()>=40

s1 = Student('jithin',[90,80,100])
s2 = Student('Anaand',[5,20,10])

print(f"{s1.name} average: {s1.average()} Passed: {s1.has_passed()}")
print(f"{s2.name} average: {s2.average()} Passed: {s2.has_passed()}")
