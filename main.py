import sqlite3
import bcrypt
try : 

     connection = sqlite3.connect('sentinel_db.sqlite')
     
     
     class User :
         def __init__(self, name : str, email : str, password_hashed: bytes):
            self.name = name
            self.email = email
            self.password_hashed = password_hashed

         @classmethod
         def create_user (cls) :
             name = input('Enter your name : ')
             email = input('Enter your mail : ')
             password = input('Enter your password : ')
             password_hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
             return cls(name, email, password_hashed)
     
     #user1 = User.create_user()
     
     #cursor = connection.cursor()
     #cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (user1.name, user1.email, user1.password_hashed))
     #connection.commit()
     
         @staticmethod
         def index () :
           cursor = connection.cursor()
           cursor.execute('SELECT * FROM users')
           metadata = cursor.fetchall()
           for data in metadata : 
            print(f'Metadata : {data}')

     User.index()



except sqlite3.Error as e : 
    print(f"L'érreur est  : {e}")