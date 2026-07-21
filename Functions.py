#Syntax of a function
'''
def func1():
    print("Hello")

#Function call : func1()
'''
#Question-1:
def greeting():
    print(user, "Have a Good Day.")

user = input("User: ")
greeting()

#Question-2: Function with Arguments
def greet(name):
    gr = "Hello!" +  name
    return gr

a = greet(" Piyush")
print(a)

#Question-3: default parameters 
def greet(name = "Stranger"):
    print(name)

greet()
greet("harry")