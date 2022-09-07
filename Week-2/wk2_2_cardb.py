# add cars to a database: e.g. make, color, type etc.
# asking using for input
#stays in memory while the program is running 

#0. Loop this
while True: 

    #1. Asking user for input on make of car
    car_make = input("what is the make of the car: ")

    #2. Ask for type of car
    car_model = input("What is the car model: ")

    #2. Ask for colour of car
    car_color = input("What is the color of the car: ")

    #4. put into dictionary

    car = {
     "make": car_make,
     "model": car_model,
     "car color": car_color
    }
    print(id(car)) # prints where it is in memory
    print(car) #shift tabe = unindent
