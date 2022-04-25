class User:
    """_user class_
    """
    #class generating new user
    user_list = []
    def __init__(self, username, password): #initializing the user
        self.username = username
        self.password = password #defining the user_login function
        """_summary_

        Args:
            username (_type_): _description_
            password (_type_): _description_
        """

    def save_user(self):
        #saving user to the user_list
        User.user_list.append(self)

