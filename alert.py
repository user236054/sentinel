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
                status = alert[6]
                alert_details = f"ID : {alert_id}\nType : {type_alert}\nAdresse IP : {address_ip}\nNom d'utilisateur : {username}\nNombre de tentative échoué : {failed_attempts}\nStatut : {status}\nDate de détection : {created_at} \n"
                
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
                status = alert[6]
                alert_details = f"ID : {alert_id}\nType : {type_alert}\nAdresse IP : {address_ip}\nNom d'utilisateur : {username}\nNombre de tentative échoué : {failed_attempts}\nStatut : {status}\nDate de détection : {created_at} \n"
                
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
    
    def status_alert() :
        alert_id = input("Entrez l'ID de l'alerte à modifier : ")
        update_status = input('Entrez le nouveau status de l\'alerte : ')
        cursor = connexion.cursor()
        
                
        if update_status in ('pending', 'resolved', 'investigating') :
                cursor.execute("UPDATE suspect_activities SET status = ? WHERE id = ?", (update_status, alert_id))
                connexion.commit()
                updated_status = cursor.rowcount
                
                if updated_status :
                
                    cursor.execute("SELECT * FROM suspect_activities WHERE id = ?", (alert_id,))
                    status_alert_updated = cursor.fetchone()
                    type_alert = status_alert_updated[1]
                    address_ip = status_alert_updated[2]
                    username = status_alert_updated[3]
                    failed_attempts = status_alert_updated[4]
                    created_at = status_alert_updated[5]
                    status = status_alert_updated[6]
                    alert_details = f"ID : {alert_id}\nType : {type_alert}\nAdresse IP : {address_ip}\nNom d'utilisateur : {username}\nNombre de tentative échoué : {failed_attempts}\nStatut : {status}\nDate de détection : {created_at} \n"
                
                    print(alert_details)
                
                else :
                    print(f"\nAucune alerte ne correspond à l\'ID saisi, veuillez réessayer ! \n")
            
        else :
            print(f"\n{update_status} n'est pas un statut valide. Les statuts valides sont : pending, investigating et resolved !\n")
            
    status_alert()
        
        
        
    
    
        
        
            
                        
            
