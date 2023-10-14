import re
import random
import string

# Colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# Password policies
MIN_PASSWORD_LENGTH = 8
REQUIRED_CHARACTER_TYPES = 3  # Number, Uppercase, Lowercase, Special Characters | Max 4

def color_text(text, color):
    """TextWrap with ANSI for color."""
    return color + text + RESET

def check_password_strength(password):
    """Check if a password meets the defined policies and give random advice."""
    advice = []

    if len(password) < MIN_PASSWORD_LENGTH:
        advice.append(color_text("Password should be at least {} characters long.".format(MIN_PASSWORD_LENGTH), RED))
    else:
        # Check for the presence of different character types
        character_types = 0
        if re.search(r'\d', password):
            character_types += 1
        else:
            advice.append(color_text("Include at least one number.", RED))

        if re.search(r'[A-Z]', password):
            character_types += 1
        else:
            advice.append(color_text("Include at least one uppercase letter.", RED))

        if re.search(r'[a-z]', password):
            character_types += 1
        else:
            advice.append(color_text("Include at least one lowercase letter.", RED))

        if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            character_types += 1
        else:
            advice.append(color_text("Include at least one special character.", RED))

        if character_types >= REQUIRED_CHARACTER_TYPES:
            advice.append(color_text("Great! Your password meets the strength criteria.", GREEN))

    return advice

def generate_strong_password():
    """Generate a random strong password."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(MIN_PASSWORD_LENGTH))
    return password

def check_passwords_from_file(filename):
    """Check a list of passwords from a text file."""
    try:
        with open(filename, 'r') as file:
            passwords = file.read().splitlines()

        for password in passwords:
            print(f"\nChecking password: {password}")
            advice = check_password_strength(password)

            for message in advice:
                print(message)

            # If the password meets both length and character type criteria, display random advice
            if color_text("Great!", GREEN) in advice and color_text("Password should be at least", RED) not in advice:
                print("\n" + color_text("Random Password Security Advice:", YELLOW))
                print(random.choice([
                    "Consider enabling Two-Factor Authentication (2FA).",
                    "Never share your password with anyone.",
                    "Avoid using default or common passwords.",
                    "Regularly update your passwords for added security."
                ]))

    except FileNotFoundError:
        print(color_text(f"File not found: {filename}", RED))

def print_ppc():
    print(color_text("""
██████╗ ██████╗  ██████╗ 
██╔══██╗██╔══██╗██╔════╝
██████╔╝██████╔╝██║     
██╔═══╝ ██╔═══╝ ██║     
██║     ██║     ╚██████╗
╚═╝     ╚═╝      ╚═════╝
  _                             _ _       
 | |                           | (_)      
 | |__  _   _    _ __ ___   ___| |_  ___  
 | '_ \| | | |  | '_ ` _ \ / _ \ | |/ _ \ 
 | |_) | |_| |  | | | | | |  __/ | | (_) |
 |_.__/ \__, |  |_| |_| |_|\___|_|_|\___/ 
         __/ |                           
        |___/                            
                          """, YELLOW))

def add_signature():
    """exit signature."""
    print(color_text("\nThanks for using the Password Policy Checker!", GREEN))
    print(color_text("Signature: ", YELLOW) + color_text("AR", GREEN))

def main():
    while True:
        print_ppc()
        print("\nOptions:")
        print("1. Check the strength of a password")
        print("2. Generate a strong password")
        print("3. Check passwords from a text file")
        print("4. Exit")

        choice = input("Enter the number of your choice (1/2/3/4): ")

        if choice == '1':
            user_password = input("Enter a password: ")
            advice = check_password_strength(user_password)

            for message in advice:
                print(message)

            # If the password meets both length and character type criteria, display random advice
            if color_text("Great!", GREEN) in advice and color_text("Password should be at least", RED) not in advice:
                print("\n" + color_text("Random Password Security Advice:", YELLOW))
                print(random.choice([
                    "Consider enabling Two-Factor Authentication (2FA).",
                    "Never share your password with anyone.",
                    "Avoid using default or common passwords.",
                    "Regularly update your passwords for added security."
                ]))
        elif choice == '2':
            new_password = generate_strong_password()
            print(f"\nGenerated Strong Password: {color_text(new_password, GREEN)}")
        elif choice == '3':
            file_name = input("Enter the name of the file containing passwords (include the extension): ")
            check_passwords_from_file(file_name)
        elif choice == '4':
            add_signature()
            break
        else:
            print(color_text("Invalid choice. Please enter 1, 2, 3, or 4.", RED))

        repeat = input("Do you want to perform another operation? (yes/no): ").lower()
        if repeat != 'yes':
            add_signature()
            break

if __name__ == "__main__":
    main()