#!/usr/bin/python3

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

users = []

def create_user():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    user = User(name, email, password)
    users.append(user)
    print("User created successfully!")

def print_users():
    for user in users:
        print(f"Name: {user.name}, Email: {user.email}, Password: {user.password}")

create_user()
print_users()

