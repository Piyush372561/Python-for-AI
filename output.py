#print("Python" or "Java")

text = input("Enter your text: ")

if "subscribe this" in text or "buy now" in text or "click this" in text or "make a lot of money" in text:
    print("This is a spam.")
else: 
    print("This is not a spam")