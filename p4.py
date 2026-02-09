'''Homework
1. List Manipulation Exercise:
• Create a list of 5 items (strings or numbers).
• Add a new item to the end of the list and another at the second position.
• Remove the third item from the list.
• Print the list after each operation.

2. Reverse and Sort a List: Create a list of numbers and:
• Sort it in descending order.
• Reverse the sorted list and print it.'''

item=["bru","milk","biscuit","juice","tea"]
print(item)
item.append("sugar")
print(item)
item.insert(2,"burbon")
print(item)
item.remove(item[3])
print(item)

items=[1,6,9,4,8,3]
print(items)
items.sort(reverse=True)
print(items)
items.reverse()
print(items)



