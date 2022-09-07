#more on functions

# def my_functions():
#     print("Hello")
    
# my_functions()    

# def my_functions1(name): # defining a function
#     print(name)
 
# my_functions1("Celle") # calling a function
 
# def my_functions2(firstname, lastname):
#     print(firstname, lastname)

# my_functions2("Celle", "Ben")

# def my_functions3(*names):
#     print(names)
    
# my_functions3("Ben", "Anuj", "Nick", "Kris", "Celle", "Tia")

# def add_all_numbers(*numbers): # * single  converts into a tuple
#    total = 0
#    for number in numbers:
#        total = total + number
#        print(total)
#    return total    
  
# total_numbers = add_all_numbers(1, 3, 5, 7) #take all inputs and put it in a tuple

# def list_all_properties(**car): # ** converts into a dictionary
#     the_input = car
#     print(f'carmaker={car["maker"]}')
#     for i in car.items():
#         print(i)
#     return car

# #python access        
# properties = list_all_properties(maker="Toyota", year="2000", model="Corolla", color="yellow")        

# def my_functions_with_default(name="nick"):
#     print(name)
# my_functions_with_default("celle")

# def dictionary_maker(**kwargs): #kwargs stands for key word arguments
#     return kwargs
 
# cars = dictionary_maker(maker="Toyota", year="2000", model="Corolla", color="yellow")

def morning():
    return "good morning"

def afternoon():
    return "good afternoon"

def greeter(time):
    if time == "sunrise":
        return morning()   
    elif time == "sunset":
        return afternoon()
    else: 
        return "unknown time"
       
# greeter("sunset")       

def greeter2(fn):
    print("running function")
    print(fn())
    print("finished running function")
    
greeter2(42)    
