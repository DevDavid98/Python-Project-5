import sys, os
from peewee import *

user_db = SqliteDatabase('users.db')
time_db = SqliteDatabase('punctual.db')


class User(Model):
    username = CharField(unique = True)
    email = CharField(unique = True)
    password = CharField()
    
    class Meta:
        database = user_db
        
    
class Punctual(Model):
    
    clock_in = DateTimeField()
    clock_out = DateTimeField()
    
    lunch_start = DateTimeField()
    lunch_end = DateTimeField()
    
    break_start = DateTimeField()
    end_break = DateTimeField()
    
    class Meta:
        database = time_db

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def start():
    while True:
        print("""
            Welcome to Punctual!
            The worlds number one time keeper.
            To start press "ENTER".
            To create your account press 'C'. 
        """)
        
        user_input = str(input('Enter your option here: '))
        if user_input == '':
            clear()
            sign_in()
        elif user_input.lower() == 'c':
            clear()
            create_user()
        else:
            clear()
            print('Please enter a valid option')
            
def create_user():
    print("""
        Enter your information below
        to create your account for Punctual.
    """)
    user_name = str(input('Username: '))
    user_email = str(input('Email: '))
    pass_word = str(input('Password: '))
    
    user_info = User.create(username = user_name, email = user_email, password = pass_word)
    user_info.save()
    clear()
    print('User created')
    
def search_user(user_name = None, user_password = None):
    attempts = 5
    all_users = User.select()
    
    if user_name and user_password:
        
        for user in all_users:
            
            if user_name == user.username:
                
                while user_password != user.password:
                    
                    user_input = input('Please enter the correct password or press "E" to exit: ')
                    
                    if user_input.lower() == 'e':
                        clear()
                        break
                        
                    elif user_input != user.password:
                        attempts -= 1
                        print('You have {} attempts left'.format(attempts))
                        
                        if attempts == 0:
                            clear()
                            print('You have exceeded the number of password attempts')
                            break
                            
                    elif user_input == user.password:
                        clear()
                        print('Welcome to punctual {}'.format(user.username))
                        logged_in() 
                        
                if user_password == user.password:
                    clear()
                    print('Welcome to punctual {}'.format(user.username))
                    logged_in()
        
            
            
def sign_in():
    all_users = User.select()
    print("""
        To get started sign in.
    """)
    user_name = str(input('Username: '))
    user_password = str(input('Password: '))
    search_user(user_name, user_password)

def logged_in():
    user_input = input('Hello: ')    

if __name__ == '__main__':
    user_db.connect()
    user_db.create_tables([User], safe=True)
    
    time_db.connect()
    time_db.create_tables([Punctual], safe=True)
    start()
