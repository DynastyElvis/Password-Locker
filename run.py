import random

from pip import main
from user import User #importing the user class

def main(): #defining the main function
    while True:
        print("\n")
        print("Hello! Welcome to Password Locker.")
        print("\n")
        print("-"*10)
        print("\n")
        print("Use these short codes : cu - create a new user, lg - login, ex - exit")
        print("\n")
        short_code = input().lower()
        if short_code == 'cu':
            print("New User")
            print("-"*10)
            print("\n")
            print("Enter your name: ")
            name = input()
            print("Enter your password: ")
            password = input()
            print("\n")
            print(f"New User {name} created")
            print("\n")
            print("-"*10)
            print("\n")
            print("Use these short codes : lg - login, ex - exit")
            print("\n")
            short_code = input().lower()
            if short_code == 'lg':
                print("Login")
                print("-"*10)
                print("\n")
                print("Enter your name: ")
                name = input()
                print("Enter your password: ")
                password = input()
                print("\n")
                print(f"Welcome {name}")
                print("\n")
                print("-"*10)
                print("\n")
                print("Use these short codes : ex - exit")
                print("\n")
                short_code = input().lower()
                if short_code == 'ex':
                    print("Exiting...")
                    break
                else:
                    print("I really didn't get that. Please use the short codes")
            else:
                print("I really didn't get that. Please use the short codes")
        else:
            print("I really didn't get that. Please use the short codes")