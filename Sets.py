s1 = set() #Like this we can create an empty set
s1.add(1)
s1.add(2)
s1.add(3)
s1.add(4)
s1.add(5)
print("Set: ",s1)


s2 = {"Piyush", "Lakshya", "Ajay", "Seema", 1, 3, 5}
print(s2)
print("This set contains",len(s2) ,"elements")
s2.remove("Piyush")
print(s2)
print(s2.pop()) #removes a random element from set
#s2.clear()
print(s2)
Union = s1.union(s2)
print(Union)

Intersection = s1.intersection(s2)
print(Intersection)

