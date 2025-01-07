import random
import string
def generate_password():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("\nEnter the desired length of the password: "))
        if length < 4:
            print("Password length should be at least 4 characters for security.")
            return
        include_uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
        include_numbers = input("Include numbers? (y/n): ").lower() == "y"
        include_symbols = input("Include symbols? (y/n): ").lower() == "y"
        characters = string.ascii_lowercase
        if include_uppercase:
            characters += string.ascii_uppercase
        if include_numbers:
            characters += string.digits
        if include_symbols:
            characters += string.punctuation
        if not characters:
            print("You must select at least one character type!")
            return
        password = "".join(random.choice(characters) for _ in range(length))
        print(f"\nGenerated Password: {password}")
    except ValueError:
        print("Error: Please enter a valid number.")
if __name__ == "__main__":
    generate_password()
