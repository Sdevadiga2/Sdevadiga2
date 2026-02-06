name="sanjana" #string
age=22 #integer
is_student=False #boolean
weight=69.5 #float
print(name)
print(age)
print(is_student)
print(weight)

print(weight)
print(type(weight))

age_float=float(age)
print(age_float) #age bocome decimal number --from 22 to 22.0--

s="100"
age=20
print(s+age) #error bcz s is string --it is in double quote--
print(int(s)+age) #no error bcz s is converted to integer

#in the same way
s="Sanjana"
age=20
print(int(s)+age) #after using int also it will not give output --bcz s is not a number it is in character form--

a=10
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)




