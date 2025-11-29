import random
import secrets
import string
import re

#Класс генирации паролей
class GenerationPassword:
    def __init__(self, len_password:int):
        self.len_password = len_password
        self.chars_number = ''.join(string.printable.split())
    
    #Метод валидации пароля
    def validation(self, user_password):
        if not bool(re.search("[a-z]", user_password)):
            return False
        if not bool(re.search("[A-Z]", user_password)):
            return False
        if not bool(re.search("[0-9]", user_password)):
            return False
        if not bool(re.search("["+ re.escape(string.punctuation)+ "]", user_password)):
            return False
        
        return True
    
    #Метод генирации пароля
    def generation_password(self):
        while True:
            password = ''.join([secrets.choice(self.chars_number) for _ in range(self.len_password)])
            if self.validation(user_password=password):
                return password