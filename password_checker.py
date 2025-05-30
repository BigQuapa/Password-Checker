from colorama import Fore, Style, init

init(autoreset = True)
#Program: Password Checker
#Created by: Shahakar Patel
#Date: 5/29/25

def check_password_strength(password):

    # Step 1: Ask the user to type a password (This step was 
    # removed since I defined the function)
    

    #Step 2: Show the entered password back
    print("You entered:", password)

    # Step 3: Check if the password is at least 8 characters

    if len(password) >=8: 
        print(Fore.GREEN + "Good: Password is long enough.")
    else:
        print(Fore.RED + "Too short: Password must be a minimum of 8 characters.")


    # Step 4: Check if the password has at least one uppcare character

    has_upper = False

    for char in password:
        if char.isupper():
            has_upper = True
            break

    if has_upper: 
        print(Fore.GREEN + "Good: Contains at least one uppercase letter.")
    else:
        print(Fore.RED + "Weak: Add at least one uppercase letter.")

    # Step 5: Check the password for at least on digit

    has_digit = False 

    for char in password:
        if char.isdigit():
            has_digit = True
            break

    if has_digit: 
            print(Fore.GREEN + "Good: Contains a number.")
    else: 
            print(Fore.RED + "Weak: Add at least one number.")

    # Step 6: Check if the password has at least one special character

    special_chars ="!@#$%^&*()-_=+{}[];:',.<>/?\|"
    has_special = False

    for char in password: 
        if char in special_chars: 
            has_special = True
            break
    if has_special: 
        print(Fore.GREEN + "Good: Contains special character.")
    else: 
        print(Fore.RED + "Weak: Add at least one more special character.")

    # Step 7: Final Strength Summary

    score = 0

    if len(password) >= 8:
        score += 1
    if has_upper: 
        score += 1
    if has_digit: 
        score += 1
    if has_special:
        score += 1

    print("\nPassword Strength Summary:")
    if score ==4:
        print("Very Strong Password.")
    elif score == 3:
        print("Medium Strength Password.")
    elif score == 2:
        print("Weak Password - Check Criteria.")
    else:
        print("Very Weak Password - Check Criteria.")

user_password = input("Enter a password: ")
check_password_strength(user_password)