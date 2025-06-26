def msg():
    print("hello")

def is_even(n):
    return n%2==0

#print(is_even(63))

'''
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.
'''

f=lambda n:n%2==0
print(f(63))