my_list = ["bread","milk", "butter", "shampoo", "milk", "bread", "bead" ]
my_fruits = "apple", "orange", "strawberry"

def addItem(item):
    return my_list.append(item)

def insertItem(item):
    return my_list.insert(2, item)

def countItem(item):
    return my_list.count(item)

def removeItem(item):
    return my_list.remove(item)

def fruits(item):
    return my_fruits.upper()

# def noOfFruits():
#     if my_fruits.count() > 2
#     return my_fruits.count()

addItem("soap")
insertItem("chocolate")
removeItem("milk")
count = countItem("chocolate")