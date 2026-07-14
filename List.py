#List is container which is used to store multiple items in a single variable. Irrespective of data type, List is mutable , ordered  and allows duplicate elements.
l1 = ["Ajay", "Piyush", "Lakshya", "Seema", 1,2,3,4]
l2 = [1,2,3,4,6]

# functions of list:
#Add leo at the end of the list
l1.append("Leo")
print(l1)

#insert Rohit at index 2
l1.insert(2,"Rohit")
print(l1)

#Removes Piyush from the list
l1.remove("Piyush")
print(l1)

#Removes the element at index 3
l1.pop(3)
print(l1)

#Sort the list
l2.sort()
print(l2)

#Reverse the existing list
l1.reverse()
print(l1)

#Insert NAVAMI at index 2
l1.insert(2,"NAVAMI")
print(l1)

#Clear the list means removes all element from list.
l1.clear()
print(l1)
