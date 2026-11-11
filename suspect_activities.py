import sqlite3
import datetime
import pdb

import banner

sentinel_banner = banner

print(sentinel_banner)

connection = sqlite3.connect('sentinel_db.sqlite')

class Suspect :
    def __init__(self) -> None:
        pass
    def catch_by_ip () :
        cursor = connection.cursor()
        
        cursor.execute("SELECT ip_address, COUNT(*) FROM connection_log WHERE status = 'failed' GROUP BY ip_address HAVING COUNT(*) >= 4" )
        connection_log = cursor.fetchall()
        
        print(f"\n----------Activités suspecte----------")
        
        for data in connection_log :
            print(f"IP suspecte : {data[0]} \nNombre de tentatives : {data[1]}")
            type_alert = 'ip'
            username = None
            ip_address = data[0]
            failed_attempts = data[1]
            created_at = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
            cursor.execute("SELECT ip_address FROM suspect_activities WHERE ip_address = ?", (ip_address,))
            ip_exit_already = cursor.fetchone()
            
            if ip_exit_already :
                print(f"\nCette alerte existe déja dans la base de donnée")
                cursor.execute("SELECT id FROM suspect_activities WHERE ip_address = ?", (ip_address,))
                id_suspect = cursor.fetchone()[0]
                
                cursor.execute("UPDATE suspect_activities SET failed_attempts = ? WHERE id = ?", (failed_attempts, id_suspect))
                
            else :
            
                cursor.execute("INSERT INTO suspect_activities (type, ip_address, username, failed_attempts, created_at) VALUES (?, ?, ?, ?, ?)", (type_alert,ip_address, username, failed_attempts, created_at))
        connection.commit()
        
                
        
    #catch_by_ip()
    
    
    def catch_by_username():
        cursor = connection.cursor()
        cursor.execute("SELECT username, COUNT (*) FROM connection_log WHERE STATUS = 'failed' GROUP BY username HAVING COUNT(*) >= 4")
        connection_log = cursor.fetchall()
        print(f"\n----------Activités suspecte----------")
        
        for data in connection_log :
            type_alert = 'username'
            ip_address = None
            suspected_username = data[0]
            failed_attempts = data[1]
            created_at = datetime.datetime.today().strftime("%d/%m/%Y, %H:%M:%S")
            print(f'Utilisateur suspect : {suspected_username} \nNombre de tentatives : {failed_attempts}')
            
            cursor.execute("SELECT * FROM suspect_activities where username = ?", (suspected_username,))
            username_already_exist = cursor.fetchone()
            
            if username_already_exist :
                print(f"\nL'alerte existe déja dans la base de donnée")
                
                cursor.execute("UPDATE suspect_activities SET failed_attempts = ? WHERE username = ?", (failed_attempts, suspected_username))
                
            else :
                cursor.execute("INSERT INTO suspect_activities (type, ip_address, username, failed_attempts, created_at ) VALUES (?, ?, ?, ?, ?)", (type_alert, ip_address, suspected_username, failed_attempts, created_at))
                
        connection.commit()
        
    catch_by_username()
        