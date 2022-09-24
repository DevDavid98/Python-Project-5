import sys, os
from peewee import *

user_db = SqliteDatabase('users.db')
time_db = SqliteDatabase('punctual.db')


class User(Model):
    username = CharField()
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
            search_user()
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
    user_email = str(input('Email: '))
    user_name = str(input('Username: '))
    pass_word = str(input('Password: '))
    
    user_info = User.create(username = user_name, email = user_email, password = pass_word)
    user_info.save()
    print('User created')
    

def confirmation(search_email = None, search_password = None):
    user_info = User.select()
    
    for item in user_info:
        if item.email == search_email:
            print('hi')
        if search_email not in item.email:
            clear()
            while True:
                user_input = input("Email does not exist would you like to create one? [Y/N]: ")
                if user_input.lower() == 'y':
                    clear()
                    create_user()
                elif user_input.lower() == 'n':
                    clear()
                    start()
                else:
                    print("Please enter a valid option.")
            
        

def search_user():
    print("""
        Please enter your information below to sign in.
    """)
    
    confirmation(str(input('Email: ')))
    confirmation(str(input('Password: ')))
    
    
    
    
    
    

if __name__ == '__main__':
    user_db.connect()
    user_db.create_tables([User], safe=True)
    
    time_db.connect()
    time_db.create_tables([Punctual], safe=True)
    start()