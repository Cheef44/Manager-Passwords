import sys
import os
sys.path.append(os.path.abspath('../src'))

from src.log_in import LogIn
from src.db import DataBase

#Класс API слоя между логикой и интерфейсом
class API:
    def __init__(self):
        pass
    
    #Вызов функции регистрации
    def registration_api(self, user_name:str, user_password:str):
        return LogIn(user_name, user_password).registration()
    
    #Вызов функции входа
    def log_in_api(self, user_name:str, user_password:str):
        return LogIn(user_name, user_password).log_in()
    
    #Вызов функции получения данных пользователя
    def data_user_api(self):
        return DataBase().retrieve_data()
    
    #Вызов функции создания таблицы паролей
    def add_password(self, name:str=None, name_sit:str=None, login:str=None, mail:bytes=None, password:bytes=None):
        return DataBase.create_passwords_db(self, name, name_sit, login, mail, password)