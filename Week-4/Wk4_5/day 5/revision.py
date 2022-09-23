#Output
import re


print("Hello")
print(1234)

#Variables
#Assigning the value 1324 to the variable foo and then printing 
foo = 1234
print(foo)

#Assigning the value "Hello" to the variable name and then print
name = "Hello"
print(name)

# Classes
# in class first letter should be capital
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
    
    def __str__(self):
        return f"Coords {self.x}, {self.y}"
    
    def __add__(self, other): 
        x = self.x + other.x
        y = self.y + other.y
        point3 = Point2D(x, y)        
        return point3
    
def point_adder(point1, point2):
        x = point1.x + point2.x
        y = point1.y + point2.y
        point3 = Point2D(x, y)        
        return point3
    
#The code is creating a Point2D object with the     
point1 = Point2D(1, 1)
print(point1)
str_point = str(point1)

point2 = Point2D(1, 1)
print(point2)
str_point = str(point2)

new_point = point_adder(point1, point2)
print(new_point)

new_point2 = point_adder(point1, point2)
print(new_point)

new_point2 = point1 + point2
print(new_point2)