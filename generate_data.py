import sqlite3
import datetime
import random
from faker import Faker
import pdb
import banner

fake = Faker(['it_IT', 'en_US','fr_FR'])
connection = sqlite3.connect('sentinel_db.sqlite')

class GenerateFakeUser :
    def __init__(self) -> None:
        pass
    
    def generatefakeuser() :
        for _in in range(10) :
            
        
            username = fake.name()
            ip_address = fake.ipv4()
            attempts = 1
            status = ["success", "failed"]
            status_random = random.choice(status)
            created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor = connection.cursor()
            cursor.execute("INSERT INTO connection_log (username, ip_address, attempts, status, created_at) VALUES(?, ?, ?, ?, ?)", (username, ip_address, attempts, status_random, created_at))
            connection.commit()
            generate = cursor.rowcount
            #pdb.set_trace()
            if generate :
                print(f"Nouvelle connexion ajouté avec succès")
                
            else :
                print(f"Erreur lors de la génération d'une nouvelle connexion")
        
        
    generatefakeuser()
        
        