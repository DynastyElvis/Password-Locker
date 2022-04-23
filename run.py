import random

"""

"""

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
            

            while confirm_password != created_password:
                print("Password does not match")
                print("Enter a password")
                created_password = input()
                print("Confirm password")#printing confirm password
                confirm_password = input()
                
                """
                
                """
            else:
                print(f"Password confirmed! Welcome {created_name} account created successfully")#printing welcome message
                print("\n")
                print("try logging in")
                print("username")
                entered_username = input()#inputing username
                print("password")
                entered_password = input()#inputing password

            while entered_username != created_name or entered_password != created_password:
                    print("wrong username or password")
                    print("username")
                    entered_username = input()
                    print("password")
                    entered_password = input()
            else:
                print(f"Welcome {entered_username}") #printing welcome message
                print("\n")
                
        elif short_code == 'lg':#if short_code is lg
            print("Login")
            print("username")
            entered_username = input()
            print("password")
            entered_password = input()
            while entered_username != created_name or entered_password != created_password:#if entered_username and entered_password are not equal to created_name and created_password
                    print("wrong username or password")
                    print("username")
                    entered_username = input()#inputing username
                    print("password")
                    entered_password = input()
            else:
                print(f"Welcome {entered_username}")#printing welcome message
                print("\n")
                print("\n")

        elif short_code == 'ex':#if short_code is ex
            print("Goodbye")#printing goodbye message
            break#break the loop
        else:
            print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':
    main()