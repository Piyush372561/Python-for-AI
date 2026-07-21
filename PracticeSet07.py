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

#Question-2: Write a program to greet all the person names stored in a list ‘lʼ and which starts with S.
l = ["Harry", "Soham", "Sachin", "Rahul"]
i = 0

while i<len(l):
     if l[i].startswith("S"):
      print("Hello! Good Morning",l[i])

     i = i + 1
    
print("Finished.")


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


#Question-6: Question-1 using for loop
n = int(input("n : "))
print("Table of :", n)


for i in range(1, 11):
    table = n * i
    print(table)
    
#Question-7: Factorial program
n = int(input("N : "))
factorial = 1
for i in range(n,0,-1):
    factorial = factorial * i

print(factorial)


#Question-8:
#Write a program to print the following star pattern:
for r in range(4):
    for c in range(2 * r - 1):
        print("*", end=" ")

    print()

#Question-9:
for i in range(4):
    for j in range(i):
        print("*", end="")
    print()


#Question-10:
for r in range(1,4):
    if(r % 2 == 0):
        for c in range(1,3):
            print("*", end="")
    else:
        for c in range(1,4):
            print("*", end="")

    print()
   '''
    
#Question-11: Write a program to print multiplication table of n using for loops in reversed order
n = int(input("n = "))

for i in range(10, 0, -1):
    table = n * i
    print(table)
