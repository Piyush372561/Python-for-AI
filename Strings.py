#we can write string in three ways in python
name = 'Piyush' #Single Quotes
name2 = "Avni" #Double Quotes
name3 = '''Leo'''  #Triple Quotes

#String Slicing
Student_name = "Piyush Kushwaha"

sl = Student_name[0:8]
print(sl)

sl2 = Student_name[-8:-1]
print(sl2)


#String Functions
Author = "piyush Kushwaha"
print(Author.count("u")) #counts the total occurence of a character in a string
print(len(Author))
print(Author.upper())
print(Author.lower())
print(Author.endswith("Kushwaha"))
print(Author.startswith("piyush"))
print(Author.replace("piyush", "Avni"))
print(Author.split(" "))
print(Author.find("Kushwaha"))
print(Author.capitalize()) #capitalizes the first character of a string
print(Author.isalpha()) #checks if the string contains only alphabets
print(Author.find("h")) #returns the index of the first occurence of a character in a string


