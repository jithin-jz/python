# Class (Student) → Blueprint for creating student objects
class Student:
    # Constructor (runs when object is created)
    def __init__(self, name, mark):
        # Attributes (name, mark) → data for each object
        self.name = name
        self.mark = mark

    # Method (introduce) → behavior of the object
    def introduce(self):
        print(f"Hi, I'm {self.name} and I got {self.mark} marks in English.")


# Objects (s1, s2) → Instances created from the class
s1 = Student("Jithin", 99)
s2 = Student("Anand", 89)

# Accessing attributes
print(s1.name, s1.mark)  # Jithin 99
print(s2.name, s2.mark)  # Anand 89

# Calling methods
s1.introduce()
s2.introduce()


# ✅ Best Practices for Python Classes

# Use clear class and method names (CapWords for class, lowercase_with_underscores for methods).

# Keep __init__ simple — only initialize attributes.

# Use __str__ or __repr__ for human-readable object representation.

# Encapsulate behavior inside methods (don’t leave all logic outside).

# Add type hints for clarity.

# Keep it minimal but clear.

class Student:
    
    def __init__(self,name:str,mark:int):
        self.name = name
        self.mark = mark
        
    def introduce(self):
        print(f'Hi im {self.name} and i got {self.mark} mark in english')
        
    def __str__(self) -> str:
        return f'Student(name={self.name},mark={self.mark})'
    
s1 = Student('JITHIN',20)
s2 = Student('ANAND',24)

print(s1)
print(s2)

s1.introduce()
s2.introduce()