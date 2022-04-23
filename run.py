import random

from user import User #importing the user class

def main(): #defining the main function
    while True:
        print("Hello! Welcome to Password Locker.")#welcome message
        print("\n")
        print("navigation shortcode: Press 'nu' to create a new account:'ex' to exit or 'lg' to login") #navigation shortcode
        short_code = input().lower() #short_code input
        print("\n") #printing a new line
       