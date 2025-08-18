import hashlib
import re
from Crypto.Random import get_random_bytes
from src import db

#Класс регистрации и входа в программу
class LogIn:
    def __init__(self, user_name:str, user_password:str):
        self.user_name = user_name
        self.user_password = user_password
        self.user_data = f"{self.user_name}{self.user_password}"
        
    #Функция регистарции
    def registration(self):
        if self.validation():
            sault_data = self.sault_func(user_name=self.user_name,user_password=self.user_password)
            sault = sault_data["sault"]
            hash_user_name = hashlib.sha3_512(bytes(self.user_name, encoding="utf-8")).digest() #Хэширование логина и пароля
            hash_user_password = hashlib.sha3_512(sault_data["sault_user_password"]).digest()

            return db.DataBase(sault=sault, user_password=hash_user_password, user_name=hash_user_name).create_login_db()    
        else:
            return False
    
    #Функция входа в программу
    def log_in(self):
        hash_user_name = hashlib.sha3_512(bytes(self.user_name, encoding="utf-8")).digest()
        user_db_data = db.DataBase(user_name=hash_user_name).retrieve_data_user()
        sault_data = self.sault_func(user_name=self.user_name, user_password=self.user_password, sault=user_db_data["sault"])
        hash_user_password = hashlib.sha3_512(sault_data["sault_user_password"]).digest()
        if user_db_data["user_name"] == hash_user_name and user_db_data["user_password"] == hash_user_password:
            return True
        else:
            return False
     
    #Генерация соли и добавление соли к данным пользователя
    def sault_func(self, user_name:str, user_password:str, sault:bytes=get_random_bytes(32)):
        user_name = bytes(user_name, encoding="utf-8")
        user_password = bytes(user_password, encoding="utf-8")
        sault_user_name = sault[:len(sault)//2]+user_name+sault[len(sault)//2:]
        sault_user_password = sault[:len(sault)//2]+user_password+sault[len(sault)//2:]
        
        return {"sault": sault, "sault_user_name": sault_user_name, "sault_user_password": sault_user_password}

    #Проверка валидации данных
    def validation(self):
        if not self.user_data or self.user_name in self.user_password:
            return False
        if not len(self.user_password) >= 8:
            return False
        if bool(re.search("[ ]", self.user_password)):
            return False
        if bool(re.search("[а-яА-ёЁ]", self.user_data)):
            return False
        if not bool(re.search("[a-z]", self.user_password)):
            return False
        if not bool(re.search("[A-Z]", self.user_password)):
            return False
        if not bool(re.search("[0-9]", self.user_password)):
            return False
        if not bool(re.search("[!-_#@%$*?/|&)}{<>+='(,)^:;№%*.]", self.user_password)):
            return False
        
        return True