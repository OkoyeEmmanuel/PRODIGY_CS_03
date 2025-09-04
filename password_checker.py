import time


    

print("1. Ensure your password is at least 8 characters long.")
time.sleep(2)

print("2. Ensure your password contains both uppercase and lowercase letters.")
time.sleep(2)

print("3. Ensure your password contains at least one digit.")
time.sleep(2)

print("4. Ensure your password contains at least one special character (e.g., !, @, #, $, etc.).")
time.sleep(2)


password_input = input("Enter your password:")
print("Checking your password length...")
time.sleep(1)

print(len(password_input))