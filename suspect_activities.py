import sqlite3

connection = sqlite3.connect('sentinel_db.sqlite')

class Suspect :
    def __init__(self) -> None:
        pass
    def catch () :
        cursor = connection.cursor()
        
        cursor.execute("SELECT * FROM connection_log")
        connection_log = cursor.fetchall()
        for data in connection_log :
            if data[4] == 'failed' :
                print(f"----------Activité suspecte---------- \n{data}")
                
        
    catch()