import sqlite3

import bcrypt
from faker import Faker

fake = Faker()

try:
    connection = sqlite3.connect("sentinel_db.sqlite")

    class User:
        def __init__(self, name: str, email: str, password_hashed: bytes):
            self.name = name
            self.email = email
            self.password_hashed = password_hashed

        @classmethod
        def store(cls):
            name = fake.name()
            email = fake.email()
            password = fake.password()
            password_hashed = bcrypt.hashpw(
                password.encode("utf-8"), bcrypt.gensalt()
            )
            return cls(name, email, password_hashed)

        @staticmethod
        def index():
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM users")
            metadata = cursor.fetchall()
            print(f"{metadata[0]}")
            for data in metadata:
                print(f"Data : {data}")

        @classmethod
        def update(cls):
            name = print("Enter your name : ")
            email = print("Enter your mail : ")
            password = print("Enter your password : ")
            password_hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
            cursor = connection.cursor()
            cursor.execute(
                "SELECT users SET name = ? email = ? password = ?",
                (name, email, password_hashed),
            )
            connection.commit()

        @staticmethod
        def delete():
            cursor = connection.cursor()
            cursor.execute(
                "DELETE FROM users WHERE name = ? email = ? "
                "password_hashed = ? (name, email, password_hashed)"
            )
            connection.commit()

    user1 = User.store()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
        (user1.name, user1.email, user1.password_hashed),
    )
    connection.commit()

    User.index()

except sqlite3.Error as e:
    print(f"L'erreur est : {e}")
