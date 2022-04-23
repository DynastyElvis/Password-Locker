import random

from user import User #importing the user class

def main(): #defining the main function
    while True:
        print("Hello! Welcome to Password Locker.")#welcome message
        print("\n")
        print("navigation shortcode: Press 'nu' to create a new account:'ex' to exit or 'lg' to login") #navigation shortcode
        short_code = input().lower() #short_code input
        print("\n") #printing a new line
       
        if short_code == 'nu': #if short_code is nu
            print("New User") #printing new user
            created_name = input

            print("Enter a password") #printing password
            created_password = input() #inputing password

            print("Confirm password") #printing confirm password
            confirm_password = input() #inputing confirm password