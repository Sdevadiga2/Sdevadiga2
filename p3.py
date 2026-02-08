'''Logical Operator Practice Write a Python program that takes two numbers as input from the user and checkst
1)Both numbers are greater than 10 (using and ).
2)At least one of the numbers is less than 5 (using or ).
3)The first number is not greater than the second (using not).

2. Comparison Operator Challenge: Create a Python program that asks the user for their age and prints:
1)"You are an adult" if the age is greater than or equal to 18.
2)"You are a minor" if the age is less than 18.
3)Use >= and comparison operators.

3. Membership Operator Exercise: Write a Python program that:
1)Takes a string as input from the user.
2)Checks if the letter 'a' is in the string (using in).
3)Checks if the string doesn't contain the word "Python" (using not in).

4. Bitwise Operator Task: Given two integers, write a Python program that:
1)Prints the result of a & b, ab, and a^b.
2)Shifts the bits of a two positions to the left (a2).
3)Shifts the bits of bone position to the right (b >> 1).'''


a=int(input("a: "))
b=int(input("b: "))
print(a)
print(b)
print(a>10 and b>10)
print(a<5 or b<5)
print(not(a>b))

user_age=int(input("age: "))
if user_age>=18:
    print("you are an adult")
else:
    print("you are an minor")

user_sentence=input("sentence: ")
if 'a' in user_sentence:
    print("yes,letter 'a' is in the given sentence")
else:
    print("letter 'a' is not in the given sentence")
if 'python' not in user_sentence:
    print("the sentence doesn't contain the word 'python' ")
else:
    print("the sentence contain the word 'python'")

a=int(input("a: "))
b=int(input("b: "))
print(a)
print(b)
print(a&b)
print(a|b)
print(a^b)
print(a<<2)
print(b>>1)
