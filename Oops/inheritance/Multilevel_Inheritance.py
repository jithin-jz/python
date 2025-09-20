# Multilevel Inheritance
# A chain of inheritance (grandparent → parent → child).

class Grandparent:
    def grandparent_trait(self):
        print('Wisdom')

class Parent(Grandparent):
    def parent_trait(self):
        print('Patience')
    
class Child(Parent):
    def child_trait(self):
        print('Playfulness')
    
c = Child()
c.grandparent_trait()
c.parent_trait()
c.child_trait()
