import keyring
import socket
import threading

#Класс кэширования данных
class CachePassword:
    def __init__(self, password=None, name_service=None, time_del_pwd=0):
        self.PASSWORD = password
        self.NAME_SERVICE = name_service
        self.time_del_pwd = time_del_pwd
        self.user_name = socket.gethostname()
    
    #Метод помещения данных в кэш
    def set_password(self):
        keyring.set_password(self.NAME_SERVICE, self.user_name, self.PASSWORD)
    
    #Метод выдачи данных из кэша
    def get_password(self):
        return keyring.get_password(self.NAME_SERVICE, self.user_name)
    
    #Метод таймера удаления данных из кэша
    def del_timer(self):
        timer = threading.Timer(self.time_del_pwd, self.del_password)
        timer.daemon = True
        timer.start()
    
    #Метод удаления данных из кэша
    def del_password(self):
        keyring.delete_password(self.NAME_SERVICE, self.user_name)
