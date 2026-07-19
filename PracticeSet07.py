#Question-1

n = int(input("n : "))
i = int(input("i : "))
print("Table of :", n)

while i <= 10:
     table = i * n
     i = i + 1
     print(table)

print("Done")

#Question-2: Write a program to greet all the person names stored in a list ‘lʼ and which starts with S.
l = ["Harry", "Soham", "Sachin", "Rahul"]
i = 0

while i<len(l):
     if l[i].startswith("S"):
      print("Hello! Good Morning",l[i])

     i = i + 1
    
print("Finished.")

#Question-3: Multiplication of a table using for loop.












#Question-4: Check a number is prime or not.(yeh humne likha tha)
num = int(input("Enter number: "))

for i in range(2, num):
   if(num % i == 0):
      print("Prime number.")
      break  
else:
   print("Composite number.")


#Question-4: 
num = int(input("Enter number: "))
is_prime = "True"

for i in range(2, num):
   if num % i == 0:
    is_prime = False
    break


if is_prime:
   print(num,"is a Prime number")
else:
   print(num,"is a Composite number.")


#Question-5:
p = int(input("Enter number: "))
i = int(input("Enter number: "))
sum = 0

while i <= p:
   sum = i + sum
   i = i + 1

print("Sum of first N natural numbers: ",sum)


   