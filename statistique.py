import sqlite3
import banner

connexion = sqlite3.connect("sentinel_db.sqlite")


class Statistique :
    def __init__(self):
        pass
    
    def total_connexion() :
        cursor = connexion.cursor()
        cursor.execute("SELECT COUNT(*) FROM connection_log")
        connexion_number = cursor.fetchone()
        #print(connexion_number)
        print(f"Nombre de connexions : {connexion_number[0]}\n")
        
    total_connexion()
    
    def total_connexion_success() :
        cursor = connexion.cursor()
        cursor.execute("SELECT COUNT(*) FROM connection_log WHERE status = 'success'")
        total_connexion_success = cursor.fetchone()
        
        print(f"Nombre de connexions réussies : {total_connexion_success[0]}\n")
            
    total_connexion_success()
    
    def total_connexion_failed() :
        cursor = connexion.cursor()
        cursor.execute("SELECT COUNT(*) FROM connection_log WHERE status = 'failed' ")
        total_connexion_failed = cursor.fetchone()
        
        print(f"Nombre de connexions échouées : {total_connexion_failed[0]}\n")
            
    total_connexion_failed()
        
        
        