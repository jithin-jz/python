# 2. Multiple Inheritance
# Child inherits from multiple parents.

class Mother:
    def mom_skill(self):
        print('Cooking')

class Father:
    def dad_skill(self):
        print('Driving')

class Child(Mother,Father):
    def child_skill(self):
        print('Gaming')
    
c = Child()
c.mom_skill()
c.dad_skill()
c.child_skill()