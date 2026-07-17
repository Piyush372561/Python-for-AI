#Question-1
'''
n = int(input("Enter the value of n:"))
i = int(input("Enter the value of i:"))

while i<n :
    print(i)
    i = i + 1


#Question-2: Write a program to print the content of a list using while loops.
l = [1,2,3,4,"Piyush", "Lakshya", "Seema"]
i = 0

while i < len(l):
    print(l[i])
    i = i + 1
'''
    
#range() function in for loop
l = [1,2,3,4,5,6,7,8,9,10]
for item in range(1,5):
  print(item) 

#break function
for i in range(0,80):
   print(i)

   if (i==3):
      break
   
#continue statement
for i in range(4):
   print("Printing")

   if i == 2:
      continue
   
print(i)

#for loop with else
l = [1,2,3]

for item in l:
    print(item)

else:
    print("Done")