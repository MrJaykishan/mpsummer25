class Car:
    wheel=4
    def __init__(self):
        self.mil = 25
        self.name = 'maruti'
    def car_info(self):
         print("name=",self.name,"milage=",self.mil,self.wheel)


c1=Car()
c1.car_info()
c2=Car()
c2.mil=55
c2.name='nano'
c2.car_info()
c1.car_info()