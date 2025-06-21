#function definition
#function with no argument
def greet():
    print("good morning")

greet()
greet()
for i in range(11):
    greet()

def add(x,y): #here x and y are called formal argument
    c=x+y
    print("Sum=",c)
    
add(2,5)
a=int(input("enter first no"))
b=int(input("enter Second number"))
add(a,b) # here and b are called actual argument int this code the actual argument value copied into formal argument
