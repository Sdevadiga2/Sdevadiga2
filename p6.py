'''Homework
1. Basic Dictionary Operations:
• Create a dictionary to store information about 5 cities in Karnataka and their famous dishes.
• Add a new city and its dish to the dictionary.
• Update the dish for Bengaluru.
• Remove one city from the dictionary.
• Use the keys() method to print all city names in the dictionary.
• Use the values() method to print all dishes in the dictionary.

2. Nested Dictionary Practice (Simple for now):
• Create a dictionary to store details of two of your friends, including their names, favorite subject, and favorite food.
• Access and print the favorite food of one friend.'''

karnataka= {
    "kundapura":"fish fry",
    "mysore":"mysore pack",
    "davangere":"bennedose",
    "chikka mangalore":"coffee",
    "mangalore":"koli rotti"
}
karnataka["tirupati"]="laddu"
print(karnataka)
karnataka["mysore"]="dose"
print(karnataka) 
karnataka.pop("chikka mangalore")
print(karnataka)
del karnataka["davangere"]
print(karnataka)
print(karnataka.keys())
print(karnataka.values())


friends={
    "Krithika":"maths,icecream",
    "Ashika":"os,chicken"
}
print(friends)
print(friends["Krithika"])
