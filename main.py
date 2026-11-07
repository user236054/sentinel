import sqlite3
from hashlib import sha256
try : 

     connection = sqlite3.connect('sentinel_db.sqlite')
     
     
     class User :
         def __init__(self, name, email, password):
            self.name = name
            self.email = email
            self.password = password

         @classmethod
         def create_user (cls) :
             name = input('Enter your name : ')
             email = input('Enter your mail : ')
             #password_hashed = sha256(password)
             password = input('Enter your password : ')
             return cls(name, email, password)
     
     user1 = User.create_user()
     
     cursor = connection.cursor()
     cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (user1.name, user1.email, user1.password))
     connection.commit()


except sqlite3.Error as e : 
    print(f"L'érreur est  : {e}")