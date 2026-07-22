#Question-1
'''
def greatest(i,j,k):
    if(i>j and i>k):
        print("I is the Greatest.")
    elif(j>i and j>k):
        print("J is the Greatest")
    else:
        print("K is the Greatest")

i = int(input("Enter I:"))
j = int(input("Enter J:"))
k = int(input("Enter K:"))

greatest(i,j,k)


#Question-2
def temp_convertion(c):
    fahrenhiet = (c * (9/5)) + 32
    print("Conertion from celsius to fahrenhiet: ",fahrenhiet)

c = int(input("Enter temp in celsius: "))
temp_convertion(c)


#Question-3
def addition(n):
   if (n == 1):
     return 1
   return sum(n-1) + n

n = int(input("n: "))
print(addition(n))
    

#Question-5
for r in range(3,0,-1):
    for c in range(r):
        print("*", end="")
    print()    


#Question-6
def Conversion(inch):
    cm = inch * 2.54
    return cm

inch = int(input("Inch : "))
cm = Conversion(inch)
print(cm)


#Question-7: Pattern
def pattern(n):
    if n == 0 :
        return 
    print("*" * n)
    pattern(n-1)


n = int(input("n: "))
pattern(n)


#Question-8:
def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n

l = ["Ajay", "Piyush", "Seema", "Lakshya", "h"]
print(rem(l, "a"))
'''

#Question-9:
def table(n):
   for i in range(1,11):
      table = i * n
      print(table)

n = int(input("n : "))
table(n)