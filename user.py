class User:
    #class generating new user
    user_list = []
    def __init__(self, name, password): #initializing the user
        self.name = name
        self.password = password #defining the user_login function


    def save_user(self):
        #saving user to the user_list
        User.user_list.append(self)

