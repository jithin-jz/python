class A:
    def a_trait(self):
        print("Trait A")


class B(A):
    def b_trait(self):
        print("Trait B")


class C(A):
    def c_trait(self):
        print("Trait C")


class D(B, C):
    def d_trait(self):
        print("Trait D")


d = D()
d.a_trait()  # Inherited through B or C
d.b_trait()
d.c_trait()
d.d_trait()
