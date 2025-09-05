import time
global bPassword
bPassword=False

print("#############################################################################")
print("Welcome to the Password Checker!")
print("1. Ensure your password is at least 8 characters long.")
time.sleep(1)

print("2. Ensure your password contains both uppercase and lowercase letters.")
time.sleep(1)

print("3. Ensure your password contains at least one digit.")
time.sleep(1)

print("4. Ensure your password contains at least one special character (e.g., !, @, #, $, etc.).")
print("#############################################################################")
time.sleep(1)


def check_password_length(password):
    return len(password) >= 8
   
def check_upper_and_lower(password):
    upper = any(c.isupper() for c in password) #the parentheses is important it calls the function
    lower = any(c.islower() for c in password)
    return upper and lower # returns true only if upper and lower are true

   
def check_digit(password):
    digit = any(c.isdigit() for c in password)
    return digit   


def check_special_character(password):
    special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
    return any(c in special_characters for c in password)


password_input = input("Enter your password:")
print("Checking password...")
time.sleep(3)

if check_password_length(password_input) == False:
    print("* Your password is too short.")
else:
    print("# Your password length is sufficient.")

if check_upper_and_lower(password_input) == True:
    print("# Your password contains both uppercase and lowercase letters.")
else:
    print("* Your password does not contain both uppercase and lowercase letters.")


if check_digit(password_input) == True:
    print("# Your password contains at least one digit.")
else:
    print("* Your password does not contain any digits.")


if check_special_character(password_input) == True:
    print("# Your password contains at least one special character.")   
else:
    print("* Your password does not contain any special characters.")

print("Processing password review...")
time.sleep(2)



