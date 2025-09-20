# Hierarchical Inheritance
# Multiple children inherit from a single parent.


class Parent:
    def common_trait(self):
        print("Common trait for all children")


class Child1(Parent):
    def trait1(self):
        print("Child1 trait")


class Child2(Parent):
    def trait2(self):
        print("Child2 trait")


c1 = Child1()
c2 = Child2()
c1.common_trait()
c2.common_trait()
