import sqlite3
import banner
import pdb


connexion = sqlite3.connect('sentinel_db.sqlite')


class ManageAlert :
    def __init__(self):
        pass
    
    def index() :
        cursor = connexion.cursor()
        cursor.execute("SELECT * FROM suspect_activities")
        suspect_activities = cursor.fetchall()
        
        if suspect_activities :
            for alert in suspect_activities :
                alert_id = alert[0]
                type_alert = alert[1]
                address_ip = alert[2]
                username = alert[3]
                failed_attempts = alert[4]
                created_at = alert[5]
                alert_details = f"ID : {alert_id}\nType : {type_alert}\nAdresse IP : {address_ip}\nNom d'utilisateur : {username}\nNombre de tentative échoué : {failed_attempts}\nDate de détection : {created_at} \n"
                
                print(alert_details)
                
        else :
            print(f"Aucune Alert n'a été détecté")
                
    #index()
    
    def show() :
        alert_id = input("Entrer l'ID de l'alerte à analyser : ")
        cursor = connexion.cursor()
        cursor.execute("SELECT * FROM suspect_activities WHERE id = ?", (alert_id,))
        connexion.commit()
        alert = cursor.fetchone()   
        
        if alert :
                type_alert = alert[1]
                address_ip = alert[2]
                username = alert[3]
                failed_attempts = alert[4]
                created_at = alert[5]
                alert_details = f"ID : {alert_id}\nType : {type_alert}\nAdresse IP : {address_ip}\nNom d'utilisateur : {username}\nNombre de tentative échoué : {failed_attempts}\nDate de détection : {created_at} \n"
                
                print(alert_details)
                        
        else :
            print(f"L'ID saisi ne correspond à aucune alerte. Veuillez réessayer ! \n")
            
    #show()
    
    
    def delete() :
        
        id_for_delete = input("Entrer l'ID de l'alerte à supprimer : ")
        cursor = connexion.cursor()
        cursor.execute("DELETE FROM suspect_activities WHERE id = ?", (id_for_delete,))
        id_deleted = cursor.rowcount
        connexion.commit()
        
        if id_deleted :
            print(f"L'alerte n°{id_for_delete} a été supprimée avec succès !")
            
        else :
            print("L'ID saisi ne correspond à aucune alerte. Veuillez réessayer !\n")
                    
    #delete()
        
        
            
                        
            
