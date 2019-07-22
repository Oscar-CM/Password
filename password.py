class Password:

    my_list = []

    def __init__(self, userName, password):
        self.userName = userName
        self.password = password
        
    def savePassword(self):
        Password.my_list.append(self)



class User:
    user_list = []

    def __init__(self, name, Password):
        self.name = name
        self.Password = Password