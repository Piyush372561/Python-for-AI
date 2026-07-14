#Tuples are pythons built-in data structure that is used to store multiple items in a single variable.
#They are ordered and unchangeable.
#They are written with round brackets.
#They can contain any data type and can also contain duplicate values.


tp = (2,4,6,8,10)
print(type(tp))
print(len(tp))
print(tp[0])
print(tp)


t2 = ("Piyush", "Rohit", "Saurabh", "Piyush", 1,2,5.6)
print(t2)
print(len(t2))
print("Type of tuple:", type(t2))

this_tuple = ("Piyush",)
print(this_tuple)
print(len(this_tuple))

this_tuple2 = tuple(("Ajay", "Lakshya", "Piyush", "Seema"))
print(this_tuple2)
print(this_tuple2[1:3])
print(this_tuple2[-3:-2])

#To determine if a sepcified item is present in a tuple we use the in keyword.
tp3 = ("IronMan","SpiderMan", "CaptainAmerica", "Thor", "Hulk")
if "Natasha RomanOff" in tp3:
    print("Yes, 'Natasha RomanOff' is in the fruits tuple")
else:
    print("No, the value is not there in tuple")

#As we know tuples are immutable but there is a workaround. We can convert the tuple in list,then change the list, and convert the list back into a tuple.
Tuple = (2,4,6,8,10)
change_in_list = list(Tuple)
change_in_list[0] = "Microsoft"
change_backin_tuple = tuple(change_in_list)

print(change_backin_tuple)

#We can not add or append more items into a tuple once we create it.
# But we can add tuple to a tuple.
old_tuple = ("Mango", "Apple", "Grapes")
z = ("Orange",)
old_tuple += z

print(old_tuple)


#tuples are immutable but we can perform all functions on it by converting it into a list and once we done adding, removing, elementys from and to it we convert that list back in tuple.

