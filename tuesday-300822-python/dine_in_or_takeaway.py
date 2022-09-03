eating = input("Are you eating in? ") #wants to know if you are dining in or ordering for takeaway.
if eating == "yes": #if the response was "yes" it triggers the next question.
    people = input("How many people will be joining you? ") #wants to know how many people are dining (max of 8).
    if people <= "8": #if the response is valid (8 or below) then it prints the following string.
        print("Perfect, please take a seat and we will be with you shortly!")
    elif people >= "8": #if the response is invalid (8 or above) then it prints the following string and ends.
        print("Sorry we don't have enough room to accomedate that amount of people. Please place your order online, Thank you!")
if eating == "no": #if the response is "no" if triggers the next question.
    takeaway = input("Would you like to make an order for delivery? ") #wants to know if you want to delievery order.
    if takeaway == "yes": #if response is "yes" then it prints the following string and ends.
        print("Please place your order online, thank you!")
    elif takeaway == "no": #if response is "no" then it prints the following string and ends.
        print("Have a good day!")  