'''
#Question-1
str1 = input("Name: ")
str2 = input("Greetings: ")
print(str1 + " " +str2)


#Write a python program to display a user entered name followed by Good Afternoon using input() function.
name = input("Enter your name: ")
print(name + ", Good Afternoon!")
 '''
#Question-2
letter = '''
Dear <|Name|>,
You are selected as a ML intern in Microsoft!
<|Date|>
'''
name = input("Enter your name: ")
date = input("Enter date: ")
print(letter.replace("<|Name|>", name).replace("<|Date|>", date))
