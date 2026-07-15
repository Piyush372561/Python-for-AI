dict_1 = {
    "Name": "Piyush",
    "Age": "20",
    "Gender": "Male"
}
print(dict_1)
print(len(dict_1))

#Functions of Dictionaries
dict_1.update({"Fathers name": "Ajay kushwaha",})
print("Updated Dictionary:", dict_1)
print(dict_1.get("name")) #get() functions print the value 
print(dict_1.items()) #item() function returns a list of key,value tuples
print(dict_1.keys()) #keys() returns a list of keys present in dictionaries
print(dict_1)
print(dict_1.values())
print(dict_1.pop("Age"))
#checks whether a key exists or not.
print("Name" in dict_1)
print("City" in dict_1)
#Check whether a key does not exist
print("City" not in dict_1)
print(sorted(dict_1))
print(dict_1.popitem())# removes and return the last inserted key-value pair
dict_1.setdefault("Role","SDE")#Returns the value of a key. If it doesn't exist, it inserts the key with a default value.
print(dict_1)
print(len(dict_1))
del dict_1["Role"] #del-Deletes a specific key or the entire dictionary.
print(dict_1)
#del dict_1 deletes the entire dictionary


#We can create a copy of a dictionary to another dictionary
New_dict = dict_1.copy()
print(New_dict)
New_dict.update({"Mothers name":"Seema Kushwaha",})
print("Updated 2nd Dictionary: ", New_dict)


#fromkeys() function Creates a new dictionary with specified keys and a common value.
Keys = ["User", "Phone no.", "Password"]
Student = dict.fromkeys(Keys, "   ")
print(Student)




