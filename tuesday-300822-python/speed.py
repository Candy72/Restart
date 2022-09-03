
# Stacey
from asyncio.events import BaseDefaultEventLoopPolicy


speed = int(input("Enter the car's speed? "))
if speed >= 100:
    print("Your speed is " +str(speed) +" please slow down")
elif speed <= 50:
    print("Your speed is " +str(speed) +" please speed up")
else:
    print("Your speed is good at " +str(speed))


# Bevan
speed = input("What is the car's current speed?")
speed = int(speed)
if speed >= 100:  
    print ("Your current speed is " +str(speed) + "km. Please slow down.")    
elif speed <= 50:
    print ("Your current speed is " +str(speed) + "km. Please speed up.")    
else:
    print ("Your current speed is " +str(speed) + "km. Good speed!")  