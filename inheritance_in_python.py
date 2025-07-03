class Room:
    def area(self,l,b):
        self.l=l
        self.b=b
        print("area=",self.l*self.b)


class GuestRoom(Room):
    def msg(self):
        print("this is guest room")


# r=Room()
# a=int(input("Enter lenght of rectangle"))
# b=int(input("Enter breadth of rectangle"))
# r.area(a,b)
g=GuestRoom()
g.msg()
g.area(55,44)