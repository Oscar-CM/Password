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

