class Password:

    my_list = []

    def __init__(self, userName, password):
        self.userName = userName
        self.password = password

    def savePassword(self):
        Password.my_list.append(self)
    
    def deletePassword(self):
        Password.my_list.remove(self)

    @classmethod
    def display_passwords(cls):
        return cls.my_list



class User:
    user_list = []

    def __init__(self, name, Password):
        self.name = name
        self.Password = Password
    
    def saveUser(self):
        User.user_list.append(self)