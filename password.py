class Password:
    '''password class
    '''

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
'''
the user credentials class
'''

class User:
    user_list = []

    def __init__(self, name, Password):
        self.name = name
        self.Password = Password

    def saveUser(self):
        User.user_list.append(self)

    @classmethod
    def check_user(cls,name,Password):
        current_user = ''
        for user in User.user_list:
            if (user.name == name and user.Password == Password):
                current_user = user.name
                return current_user

