import sqlite3

import bcrypt
#from faker import Faker

#fake = Faker()

try:
    connection = sqlite3.connect("sentinel_db.sqlite")

    class User:
        def __init__(self, name: str, email: str, password_hashed: bytes):
            self.name = name
            self.email = email
            self.password_hashed = password_hashed
                

    
    
    class UserManager : 
        @staticmethod
        def index():
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM users")
            data = cursor.fetchall()
            for users in data:
                print(f"Users : {users}")
                
    
    
        @staticmethod
        def store():
            
            name = input("Enter your name : ")
            email = input("Enter your email : ")
            password = input("Enter your password : ")
            password_hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
            return User(name, email, password_hashed)
        
    user = UserManager.store()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)",(user.name, user.email, user.password_hashed),)
    connection.commit()
        
        @staticmethod
        def show ()  :
            user_id = int(input("Enter your id : "))
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
            return cursor.fetchone()
        
        user = UserManager.show(user_id)
        if user :
            print(f"Utilisateur : {user}")
            
        else :
            print(f"Aucun utilisateur trouvé avec l'id : {user_id}")
        
        
        @staticmethod
        def update (cls, user_id) :
            name = input("Enter your new name : ")
            email = input("Enter your new email : ")
            password = input("Enter your new password : ")
            password_hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            cursor = connection.cursor()
            cursor.execute("UPDATE users SET name = ?, email = ?, password = ?  WHERE id = ?",(name, email, password_hashed, user_id))
            connection.commit()
            return User(name, email, password_hashed)
    User_updated = UserManager.update(user_id)
    UserManager.index(user_id)
    
    
        @staticmethod
        def delete (user_id) :
            #print("Enter your id : ")
            cursor = connection.cursor()
            cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
            connection.commit()
            
            return cursor.rowcount
            
    user_deleted = UserManager.delete(user_id)
    
    if cursor.rowcount :
        print(f"Utilisateur {user_id} supprimé avec succès")
        
    else :
        print(f"Aucun utilisateur ne correspond à l'id {user_id}")
        


except sqlite3.Error as e:
    print(f"L'erreur est : {e}")
