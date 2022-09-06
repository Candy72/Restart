#dictionaries
my_dictionary = {"Luke": 50, "Nick": 100,"Anuj": 44} 

for key in my_dictionary.keys():
    print(key)
for value in my_dictionary.values():
    print(value)
for item in my_dictionary.items():
    print(item)       #lines 8 and 11 are the same as line 14 by itself
    print(f"{item[0]} is {item[1]}")
    key, value = item
    print(f"{key} is {value}")

for key, value in my_dictionary.items(): # Tuple unpacking
    print(key)
    print(value)
    