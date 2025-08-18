from src.log_in_interface import Ui_log_in
from src.main_window_interface import Ui_MainWindow
from src.dialog_add_password_interface import Ui_Add_password
from PyQt6.QtWidgets import QMainWindow, QDialog
from src.api import API
from src.table_model import PasswordsTabel
from PyQt6.QtWidgets import QHeaderView
from PyQt6.QtCore import pyqtSignal, pyqtSlot

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
                self.swap_mainwindow()
    
    #Взаимодействие функции входа в программу с интерфейсом через API
    def log_in_button(self):
        if self.password_input_1.text() == self.password_input_2.text():
            if API.log_in_api(self, user_name=self.login_input.text(), user_password=self.password_input_1.text()):
                self.swap_mainwindow()
    
    #Функция перехода на основное окно
    def swap_mainwindow(self):
        self.close()
        self.window = MainWindow(self.login_input.text())
        self.window.show()

#Класс функциональности интерфейса основного окна 
class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, user_name_data):
        super().__init__()
        self.setupUi(self)
        self.user_name_data = user_name_data
        self.user_name.setText(user_name_data)
        self.update_table()
        self.add_data.clicked.connect(self.open_dialog_add_password)
    
    #Открытие диалогового окна
    @pyqtSlot()
    def open_dialog_add_password(self):
        dialog_window = DialogAddPassword()
        dialog_window.saved_table_passwords.connect(self.update_table)
        dialog_window.exec()
    
    #Функция обнавления таблицы паролей
    @pyqtSlot(bool)
    def update_table(self):
        data = API.data_passwords_api(self)
        if data:
            header = ["Имя записи", "Имя сайта/ссылка", "Логин", "Почта", "Пароль"]
            model_table = PasswordsTabel(data, header)
            self.table_passwords.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
            self.table_passwords.setModel(model_table)
        

#Диалоговое окно добавления пароля
class DialogAddPassword(Ui_Add_password, QDialog):
    #Сигнал сохранения записи в базе данных
    saved_table_passwords = pyqtSignal(bool)
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        try:
            self.buttonBox.accepted.disconnect()
        except TypeError:
            pass
        self.buttonBox.accepted.connect(self.required_fields_validator)
    
    #Валидатор обязательных полей
    @pyqtSlot()
    def required_fields_validator(self):
        if not self.password_input.text().split():
            self.password_input.setStyleSheet("border: 1px solid red;")
        else:
            API.add_password(self, self.name_input.text(), self.sit_input.text(), self.login_input.text(), bytes(self.email_input.text(), encoding="utf-8"), bytes(self.password_input.text(), encoding="utf-8"))
            self.saved_table_passwords.emit(True)
            self.accept()