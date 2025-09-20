# Single Inheritance – Child inherits from one parent
class Parent:
    def __init__(self,name) -> None:
        self.name = name
        
    def greet(self):
        print(f'Hello i am {self.name}')

class Child(Parent):
    def play(self):
        print(f'{self.name} is playing')

c = Child('Jithin')
c.greet()
c.play()

# Child inherits from one parent.
class Parent:
    def greet(self):
        print("Hello from Parent")


class Child(Parent):
    def greet_child(self):
        print("Hello from Child")


c = Child()
c.greet()  # Inherited from Parent
c.greet_child()  # Defined in Child
