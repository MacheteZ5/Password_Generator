from random import choice
from string import ascii_letters, digits, punctuation


def main():
    characters = ascii_letters + digits + punctuation
    password = ""
    while True:
        password_length_string = input("Enter the password length: ")
        if password_length_string.isdigit() and int(password_length_string) > 0:
            break
        else:
            print("Error: The value to be entered must be a positive integer.")
    for index in range(int(password_length_string)):
        password += choice(characters)
    print(password)


if __name__ == "__main__":
    main()
