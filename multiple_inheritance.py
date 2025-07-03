class Theory:
    def t_marks(self):
        print("This is t marks ")

class Sessional:
    def s_marks(self):
        print("This is s marks ")

class Result(Theory,Sessional):
    pass
r=Result()
r.t_marks()
r.s_marks()