myString = input("Enter a String: ")

print("Length of the given sting", len(myString))

print("Converting the given string to Uppercase", myString.upper())

print("Converting the given string to Lowercase", myString.lower())

print("Capitalizing the given string", myString.capitalize())

print("Converting the given string to Titlecase", myString.title())

print("Removing whitespaces", myString.strip())

subString = input("Enter a substring: ")

print("Finding the index of given substring in myString", myString.find(subString))

print("Returning the individual subStrings", myString.split(" "))