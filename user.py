class User:
    #class generating new user
    user_list = []
    def __init__(self, name, password):
        self.name = name
        self.password = password


    def save_user(self):
        #saving user to the user_list
        User.user_list.append(self)

