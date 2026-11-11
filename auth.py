
import sqlite3
import socket 
import datetime
import banner

connection = sqlite3.connect('sentinel_db.sqlite')
class Login :
    def __init__(self, name, email, password):
        pass
    
    def store () :
        username =  input('Enter your username : ')
        host = socket.gethostname()
        ip_address = socket.gethostbyname(host)
        created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        attempts = 1
        status = 'failed'
        
        
        
        cursor = connection.cursor()
        cursor.execute("INSERT INTO connection_log (username, ip_address, attempts, status, created_at) VALUES(?, ?, ?, ?, ?)", (username, ip_address, attempts, status, created_at) )
        connection.commit()
        return cursor.fetchone()
    
    store()
    
    def index() :
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM connection_log")
        datas = cursor.fetchall()
        
        for data in datas : 
            print(f"Data : {data}")
        
    #index()
    
    def show() :
        log_id = input("Enter your id : ")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM connection_log WHERE id = ?", (log_id,))
        connection.commit()
        log = cursor.fetchone()
        if log :
            print(f"Log : {log}")
            
        else :
            print("Aucun événement ne correspond à cet ID")
            
    #show()
    
    def update() :
        cursor = connection.cursor()
        log_id = input('Enter your id for update : ')
        username = input('Enter your new username : ')
        ip_address =input('Enter your new ip_address : ')
        status = input('Enter your new status (success/failed) : ')
        if status in ('success', 'failed') :
            cursor.execute("UPDATE connection_log SET username = ?, ip_address = ?, status = ? WHERE id = ?", (username, ip_address, status, log_id))
            connection_update = cursor.rowcount
            connection.commit()
            
            if connection_update :
                print(f"Un evenement à été modifier avec succès")
                
            else :
                print(f"Aucun événement ne correspond à l'ID : {log_id}")
            
        else :
            print(f"Statut invalid")
            
    #update()
            
    
    def delete() :
        
        log_id = input("Enter id for delete : ")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM connection_log WHERE id = ?", (log_id,))
        connection.commit()
        log_deleted = cursor.rowcount
        
        if log_deleted :
            print(f"Evenement supprimé avec succès")
            
        else :
            print(f"Aucun événement ne correspond à cet ID.")
            
    #delete()
        
        
            
        