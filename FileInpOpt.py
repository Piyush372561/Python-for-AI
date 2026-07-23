'''
#create and read a file.
f = open("file.txt")
r = f.read()
print(r, type(r))
f.close()

#write in file
fw = open("file.txt", "w")
w = fw.write("I am a StoryTeller. ")
print(w)
f.close()
'''

#creating a file using with statement 
with open("file.txt")as f:

    #Read the contents of the file.
    text = f.read()

    #Print the contents.
    print(text)

    



