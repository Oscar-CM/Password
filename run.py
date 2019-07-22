from password import Password, User
import random
import string

def create_password(name, passw):
    new_creation = Password(name,passw)
    return new_creation

def savePass(details):
    details.savePassword()

def display_passwords():
    return Password.display_passwords()

def createCred(name, Password):
    new_user = User(name, Password)
    return new_user

def saveCredentials(details):
    details.saveUser()

def verify_user(first_name,password):
	
	checking_user = User.check_user(first_name,password)
	return checking_user

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def main():
    print("WELCOME TO THE PASSWORD VAULT")
    print("-"*30)

        while True:
        print("Take sometime to authenticate yourself")
        print("Use either 1,2,3 to navigate. \n 1--Create a pass lock account \n 2--Log in \n 3--Exit")
        code = input("Enter your choice").lower()
        if code == "1":
                print("Enter Username")
                name = input()
                print("Enter referred password")
                password = input()

                saveCredentials(createCred(name,password))

                print(f"{name}, your credentials have been saved successfully")
        elif code =='3':
            print("Byee.....")
            break

        elif code == "2":
            print("Enter user Name")
            name = input()
            print("Enter password")
            passw = input()
            user_exists = verify_user(name,passw)
            if user_exists == name:
                print(" ")
                print(f'Welcome {name}.\n Please choose an option to continue.')
                print(' ')
          


