import sys
import os
sys.path.append(os.path.abspath('../src'))

from src.log_in import LogIn
from src.db import DataBase
from src.generation_keys import Keys
from src.encryption import EncryptionText
from src.decryption import Decryption
from src.csv_import import PasswordCSV
import webview
import base64

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
        return DataBase().retrieve_data_user()
    
    #Вызов функции получения данных паролей
    def data_passwords_api(self):
        data = []
        for value in DataBase().retrieve_data_passwords():
            str_data = []
            for i in value:
                try:
                    str_data.append(base64.b64encode(i).decode('utf-8'))
                except TypeError:
                    str_data.append(i)
            data.append(str_data)
        return data 
    
    #Вызов функции создания таблицы паролей
    def add_password_api(self, name:str=None, name_sit:str=None, login:str=None, mail:bytes=None, password:bytes=None):
        return DataBase.create_passwords_db(self, name, name_sit, login, mail, password)
    
    #Вызов функции обновления таблицы паролей
    def uptade_password_api(self, id:int, name:str=None, name_sit:str=None, login:str=None, mail:bytes=None, password:bytes=None):
        return DataBase.update_password(self, id, name, name_sit, login, mail, password)
    
    #Вызов функции генерации ключей шифрования
    def keys_generation_api(self):
        Keys().run()
    
    #Вызов функции шифрования текста    
    def encryption_data_api(self, data:str):
        return EncryptionText(data).encryption_text()
    
    #Вызов функции дешифровки данных
    def decryption_data_api(self, data:bytes):
        return Decryption(data).decryption()
    
    #Вызов функции удаления данных
    def del_data_api(self, id:int):
        return DataBase.del_data(self, id)
    
    #Вызов функции сериализации данных из файла csv
    def import_csv_passwords_api(self, file_name):
        return PasswordCSV(file_name).processing_csv()
    
    #Функция переключения окна
    def open_html_inteface_api(self, url):
        webview.windows[0].load_url(url)
        return True
    
    #Функция изменения размера окна веб-интерфейса
    def resize_window_api(self, width, height):
        window = webview.windows[0]
        window.resize(width, height)
        return True