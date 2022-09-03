attemptsleft = 3
while True:
    if attemptsleft <= 0:
        print("No attempts left, you are blocked")
        break
    else:
        password = input("Please enter your password?")
        if password == "abc123":
            print("Welcome to the admin console")
        else:
            print("Password incorrect, remaining attempts: " + str(attemptsleft))
            attemptsleft = attemptsleft - 1