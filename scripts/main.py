from src.log_in_interface import Ui_log_in
from PyQt6.QtWidgets import QMainWindow
from src.api import API

#Класс функциональности интерфейса регистрации и авторизации
class LogInApp(Ui_log_in, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.registration.clicked.connect(self.registration_button)
        self.log_in_2.clicked.connect(self.log_in_button)
        
    #Взаимодействие функции регистрации с интерфейсом через API
    def registration_button(self):
        if self.password_input_1.text() == self.password_input_2.text():
            if API.registration_api(self, user_name=self.login_input.text(), user_password=self.password_input_1.text()):
                pass
    
    #Взаимодействие функции входа в программу с интерфейсом через API
    def log_in_button(self):
        if self.password_input_1.text() == self.password_input_2.text():
            if API.log_in_api(self, user_name=self.login_input.text(), user_password=self.password_input_1.text()):
                pass