"""
function-group of related statement that perfom a specific task
1.predefined function e.g print,range,len,input
2.user defined
in python ,a fuction is declared using the def keyword,followed by an identifier(use rules of naming variables/functions)
"""
a=10
b=20
print(a+b)
# simple function
# def saySomething():
#     """This function print out a statement"""
#     print("A Function has been created")
#     print("This is fun!")
#     # to use ou above function,we need to call it below
# saySomething()
# saySomething()
#  a function that take in parameter
def addTwoNumbers(x,y):
    print(x+y)

addTwoNumbers(100,1000)
addTwoNumbers(-10,10)
# subtract
def subtractTwoNumbers(e,f):
    print(e-f)

subtractTwoNumbers(40,50)
subtractTwoNumbers(100,60)
# MULTIPLY
def multiplyTwoNumbers(g,h):
    print(g*h)
multiplyTwoNumbers(20,10)
