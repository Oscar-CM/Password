from password import Password, User
import random
import string

'''
Methods for different futionalities
'''

def create_password(name, passw):
    '''
    save password functionality
    '''
    new_creation = Password(name,passw)
    return new_creation

def savePass(details):
    details.savePassword()

def display_passwords():
    '''
    display all the saved passwords
    '''
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

    '''
    Authenticate the user
    '''

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
          
                '''
                Save and display the user details
                '''


                while True:
                    print("Use the following shoryt codes : \n AD--to add new password, \n DA-- to display all the details, \n AN - to add new account details, \n E - Exit")
                    print("")
                    print("Enter the short code")
                    shortCode = input().lower()
                    if shortCode == "ad":
                        print("New Details")
                        print("-"*10)

                        print("Name")
                        name = input()

                        print("Password")
                        passw = input()

                        savePass(create_password(name,passw))
                        print('\n')


                        print("It has been added successfully")
                    elif shortCode =="e":
                        print("Byee.....")
                        break

                    elif shortCode == 'da':
                        if display_passwords():
                            print ("Here is a list")

                            for password in display_passwords():
                                print(f"{password.userName} { password.password}")
                            print("\n")

                        else:
                            print("Sorry")
                    elif shortCode =='an':
                        print("Enter account Name")
                        name = input()
                        print("Choose the code AA -- to enter your own password or BB -- for the system to generate your password")
                        my_code = input().lower()
                        '''
                        Have the option to either ednter their owm password or choose let the program generate
                        '''


                
                        if(my_code == "aa"):
                            print('Enter your password')
                            passw = input()
                            savePass(create_password(name,passw))
                            print("Your details have been enetered successfully")
                        elif(my_code == "bb"):
                            passw = randomString(8)
                            savePass(create_password(name,passw))
                            print("Your details have been enetered successfully")
                            

                        
                    

                    else:
                            print("Enter the appropriate shortcode")
                    
            else:
                print("The log in details are wrong")
                print("Try again")
                print('*'*40)
          

       


if __name__ == '__main__':
    main()

