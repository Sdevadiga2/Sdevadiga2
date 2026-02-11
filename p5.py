'''Homework
1. Tuple Operations:
Create a tuple with 5 elements.
Try to modify one of the elements. What happens?
Perform slicing on the tuple to extract the second and third elements.
Concatenate the tuple with another tuple.

2. Set Operations:
Create two sets: one with your favorite fruits and another with your friend's favorite fruits.
Find the union, intersection, and difference between the two sets.
Add a new fruit to your set.
Remove a fruit from your set using both remove() and discard(). What happens when the fruit doesn't exist?

3. Tuple and Set Comparison:
Create a list of elements and convert it into both a tuple and a set.
 Print both the tuple and the set.
Try to add new elements to the tuple and set. What differences do you observe?'''

#tuples
tuple1=("hi","hello","hlo","guys","how")
print(tuple1)
print(tuple1[1:3])
tuple2=("good","morning")
new_tuple=tuple1+tuple2
print(new_tuple)

#sets
my_favfruit={"chikku","apple","cherry"}
friends_favfruit={"mango","pineapple","chikku","pomogranate","apple"}
print(my_favfruit)
print(friends_favfruit)
a=my_favfruit|friends_favfruit
print(a)
b=my_favfruit&friends_favfruit
print(b)
c=my_favfruit-friends_favfruit
print(c)
my_favfruit.add("sapota")
print(my_favfruit)
my_favfruit.discard("pineapple")
print(my_favfruit)
my_favfruit.remove("pineapple")
print(my_favfruit)

