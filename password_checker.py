import time
global bPassword
bPassword=False

print("1. Ensure your password is at least 8 characters long.")
time.sleep(2)

print("2. Ensure your password contains both uppercase and lowercase letters.")
time.sleep(2)

print("3. Ensure your password contains at least one digit.")
time.sleep(2)

print("4. Ensure your password contains at least one special character (e.g., !, @, #, $, etc.).")
time.sleep(2)


def check_password_length(password):
    return len(password) >= 8
   

password_input = input("Enter your password:")

print("Checking your password length...")
check_password_length(password_input)
time.sleep(1)

print("Checking for uppercase and lowercase letters...")

time.sleep(1)

print("Checking for at least one digit...")

time.sleep(1)

print("Checking for at least one special character...")
time.sleep(1)


print("Password check complete.")
time.sleep(1)
print("Password Review:")


if check_password_length(password_input):
    bPassword=True
    print("Your password meets the length requirement.")