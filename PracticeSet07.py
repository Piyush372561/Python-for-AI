#Question-1
'''
n = int(input("n : "))
i = int(input("i : "))
print("Table of :", n)

while i <= 10:
     table = i * n
     i = i + 1
     print(table)

print("Done")
'''
#Question-2: Write a program to greet all the person names stored in a list ‘lʼ and which starts with S.
l = ["Harry", "Soham", "Sachin", "Rahul"]
i = 0

while i<len(l):
     if l[i].startswith("S"):
      print("Hello! Good Morning",l[i])

     i = i + 1
    
print("Finished.")

#Question-3: 












#Question-4: Check a number is prime or not.
num = int(input("Enter number: "))

for i in range(2, num):
   if(num % i == 0):
      print("Prime number.")
      
else:
   print("Composite number.")