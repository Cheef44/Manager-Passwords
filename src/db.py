import sqlite3

class DataBase:
    def __init__(self, sault=None, user_password = None, user_name = None) -> None:
        self.sault = sault
        self.user_password = user_password
        self.user_name = user_name
    
    def create_login_db(self):
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS user(
                sault TEXT,
                user_name TEXT,
                user_password TEXT);
            """)
            
            cursor.execute("INSERT INTO user(sault, user_name, user_password) VALUES(?, ?, ?);", (self.sault, self.user_name, self.user_password))
            cursor.close()
            conn.commit()
            return True