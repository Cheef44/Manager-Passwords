import sqlite3

#Класс ьазы данных
class DataBase:
    def __init__(self, sault:bytes=None, user_password:bytes=None, user_name:bytes=None) -> None:
        self.sault = sault
        self.user_password = user_password
        self.user_name = user_name
    
    #Функция создания таблицы
    def create_login_db(self):
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS user(
                sault BLOB,
                user_name BLOB,
                user_password BLOB);
            """)
            
            cursor.execute("INSERT INTO user(sault, user_name, user_password) VALUES(?, ?, ?);", (self.sault, self.user_name, self.user_password))
            cursor.close()
            conn.commit()
            return True
    
    #Функция создания таблицы паролей
    def create_passwords_db(self, name:str=None, name_sit:str=None, login:str=None, mail:bytes=None, password:bytes=None):
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS password(
                name TEXT,
                name_sit TEXT,
                login TEXT,
                mail BLOB,
                password BLOB NOT NULL);
            """)
            
            cursor.execute("INSERT INTO password(name, name_sit, login, mail, password) VALUES(?, ?, ?, ?, ?);", (name, name_sit, login, mail, password))
            cursor.close()
            conn.commit()
            return True
            
    #Функция получения данных из таблицы пользователя
    def retrieve_data_user(self):
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            if self.user_name:
                sault = cursor.execute("SELECT sault FROM user WHERE user_name = ?;", (self.user_name,)).fetchall()
            else:
                sault = [[[]]]
            user_name = cursor.execute("""SELECT user_name FROM user""").fetchall()
            user_password = cursor.execute("""SELECT user_password FROM user""").fetchall()
            return {
                "sault":sault[0][0],
                "user_name":user_name[0][0],
                "user_password":user_password[0][0]
                }
    
    #Функция получения данных из таблицы паролей
    def retrieve_data_passwords(self):
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            passwords = cursor.execute("SELECT * FROM password;").fetchall()
            return passwords