#Question-1
'''
Words = {
    "Madad" : "Help",
    "Pata" : "Address",
    "Gaaon" : "Village",
}
Word = input("Enter the you want to know the meaning: ")

print(Words[Word])


#Question-2
s = set()
n = input("Enter no. 1: ")
s.add(int(n))
n = input("Enter no. 2: ")
s.add(int(n))
n = input("Enter no. 3: ")
s.add(int(n))
n = input("Enter no. 4: ")
s.add(int(n))
n = input("Enter no. 5: ")
s.add(int(n))
n = input("Enter no. 6: ")
s.add(int(n))
n = input("Enter no. 7: ")
s.add(int(n))
n = input("Enter no. 8: ")
s.add(int(n))

print("Set : ", s)



#Question-3
s1 = set()
s1.add(18)
s1.add("18")

print(s1)

#Question-4
#Lenth of s2 will be 
s2 = set()
s2.add(20)
s2.add(20.0)
s2.add("20")

print(len(s2))
print(s2)

#Question-5
s3 = {} #dictionary type
print(type(s3))

'''


#Question-6
dictionary = {}

name = input("Enter Friends name: ")
Lang = input("Enter Language name: ")

dictionary.update({name: Lang})

name = input("Enter Friends name: ")
Lang = input("Enter Language name: ")

dictionary.update({name: Lang})

name = input("Enter Friends name: ")
Lang = input("Enter Language name: ")

dictionary.update({name: Lang})

name = input("Enter Friends name: ")
Lang = input("Enter Language name: ")

dictionary.update({name: Lang})


print(dictionary)

#Question-9 : Can you change the values inside a list which is contained in set S?
s = {8,7,12, "Piyush", [1,2]}

#we can not change the because how can you put list into a set because list is changeable and ordered where sets are not








