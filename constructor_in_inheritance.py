class A:
    def __init__(self):
        print("This is class A constructor")

class B(A):
     def __init__(self):
         super().__init__()
         print("This is class B constructor")
class C(B):
    def __init__(self):
        super().__init__()
        print("This is class C constructor")
c=C()