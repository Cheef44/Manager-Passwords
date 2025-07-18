import json
import hashlib
import re

#Класс регистрации и входа в программу
class LogIn:
    def __init__(self, user_name:str, user_password:str):
        self.user_name = user_name
        self.user_password = user_password
        self.user_data = f"{self.user_name}{self.user_password}"
        
    def registration(self):
        pass

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