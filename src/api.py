import sys
import os
sys.path.append(os.path.abspath('../src'))

from src.log_in import LogIn

#Класс API слоя между логикой и интерфейсом
class API:
    def __init__(self):
        pass
    
    #Вызов функции регистрации
    def registration_api(self, user_name:str, user_password:str):
        return LogIn(user_name, user_password).registration()