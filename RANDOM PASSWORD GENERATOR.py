import random
import string

def generate_password(length):
    """
    Generates a random password of a specified length.
    """
    
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    
    all_characters = letters + digits + symbols

    
    if length <= 0:
        return "Error: Password length must be a positive number."

    
    password = ''.join(random.choices(all_characters, k=length))
    return password

if __name__ == "__main__":
    try:
        
        password_length = int(input("Enter the desired password length: "))

        
        new_password = generate_password(password_length)
        print(f"Generated password: {new_password}")

    except ValueError:
        print("Invalid input. Please enter a number for the password length.")