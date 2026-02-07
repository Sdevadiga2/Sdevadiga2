#Homework
'''1)Simple Greeting Program: Write a Python program that asks the user for their name and age, then prints a personalized greeting message. Use both the + operator and f-strings for output.
Example:
Enter your name: Alice
Enter your age: 25
Output: Hello, Alice! You are 25 years old.
String Manipulation Exercise: Write a Python program that:

2)Takes a sentence as input from the user.
Prints the sentence in all uppercase and lowercase.
Replaces all spaces with underscores.
Removes leading and trailing whitespace.
Example:
Input: "   Python is awesome!   "
Output:
Uppercase: "PYTHON IS AWESOME!"
Lowercase: "python is awesome!"
Replaced: "Python_is_awesome!"
Stripped: "Python is awesome!"

3)Character Counter: Write a Python program that:
Asks the user for a string.
Prints how many characters are in the string, excluding spaces.
Example:
Input: "Hello World"
Output: "Number of characters (excluding spaces): 10"

4)Escape Sequence Practice: Write a Python program that uses escape sequences to print the following output:
Example:
Hello
    World
This is a backslash: \
'''

user_name="Alice"
user_age=25
print("hello, " + user_name + "! you are 25 years old.")

message=input("sentence: ")
print(message)
print(message.upper())
print(message.lower())
print(message.replace(" ",'_'))
print(message.strip()) #doubt and not working

line=input("line: ")
print(line)
length=len(line)
print("Number of characters (excluding spaces): " + str(length))

input="Hello\n world"
print(input)

