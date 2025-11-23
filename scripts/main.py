from src.log_in_interface import Ui_log_in
from src.main_window_interface import Ui_MainWindow
from src.dialog_add_password_interface import Ui_Add_password
from src.dialog_csv_import_interface import Ui_Dialog
from src.dialog_csv_export_interface import Export_Ui_Dialog
from PySide6.QtWidgets import QMainWindow, QDialog, QFileDialog
from src.api import API
from src.table_model import PasswordsTabel
from PySide6.QtWidgets import QHeaderView
from PySide6.QtCore import Signal, Slot
import logging
from src.create_context_menu import ContextMenu
from PySide6.QtCore import Qt
import json
import os

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
        API.keys_generation_api(self)
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
        self.setMouseTracking(True)
        self.update_table()
        self.add_data.clicked.connect(self.open_dialog_add_password)
        self.table_passwords.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.table_passwords.customContextMenuRequested.connect(self.del_context_menu)
        self.csv_import.clicked.connect(self.open_dialog_import_passwords)
        self.csv_export.clicked.connect(self.open_dialog_export_passwords)
    
    #Открытие диалогового окна
    @Slot()
    def open_dialog_add_password(self):
        dialog_window = DialogAddPassword()
        dialog_window.saved_table_passwords.connect(self.update_table)
        dialog_window.exec()
    
    #Функция обнавления таблицы паролей
    @Slot(bool)
    def update_table(self):
        data = API.data_passwords_api(self)
        if data:
            header = ["ID","Имя записи", "Имя сайта/ссылка", "Логин", "Почта", "Пароль"]
            model_table = PasswordsTabel(data, header)
            self.table_passwords.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
            self.table_passwords.setModel(model_table)
    
    #Контекстное меню удаления строки в таблице
    def del_context_menu(self, position):
        index = self.table_passwords.indexAt(position)
        ContextMenu(menu={"Удалить": lambda: API.del_data_api(self, str(index.row()+1))})
        self.table_passwords.model().removeRow(row=index.row())
    
    #Метод открытия окна импорта паролей из csv файла
    @Slot()
    def open_dialog_import_passwords(self):
        dialog_windows = DialogImportPasswords()
        dialog_windows.saved_table_passwords_csv.connect(self.update_table)
        dialog_windows.exec()
    
    #Метод открытия окна экспорта паролей в csv файл
    def open_dialog_export_passwords(self):
        dialog_windows = DialogExportPasswords()
        dialog_windows.exec()
        

#Диалоговое окно добавления пароля
class DialogAddPassword(Ui_Add_password, QDialog):
    #Сигнал сохранения записи в базе данных
    saved_table_passwords = Signal(bool)
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        try:
            self.buttonBox.accepted.disconnect()
        except TypeError:
            pass
        self.buttonBox.accepted.connect(self.required_fields_validator)
    
    #Валидатор обязательных полей
    @Slot()
    def required_fields_validator(self):
        if not self.password_input.text().split():
            self.password_input.setStyleSheet("border: 1px solid red;")
        else:
            enc_password_input = API.encryption_data_api(self, self.password_input.text())
            enc_email_input = API.encryption_data_api(self, self.email_input.text())
            API.add_password_api(self, self.name_input.text(), self.sit_input.text(), self.login_input.text(), enc_email_input, enc_password_input)
            self.saved_table_passwords.emit(True)
            self.accept()
            self.saved_table_passwords.emit(False)

#Класс диалогового окна импорта паролей
class DialogImportPasswords(Ui_Dialog, QDialog):
    #Сигнал сохранения записи в базе данных
    saved_table_passwords_csv = Signal(bool)
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        try:
            self.buttonBox.accepted.disconnect()
        except TypeError:
            pass
        self.button_dir.clicked.connect(self.open_dialog_file)
        self.buttonBox.accepted.connect(self.import_csv_passwords)
    
    #Метод открытия окна файлового менеджера    
    def open_dialog_file(self):
        csv_path = "C:/"
        with open("config\config.json", "r") as config:
            config_file = json.load(config)
        try:
            csv_path = config_file["path"]["default_csv_path"]
        except:
            config_file["path"]["default_csv_path"] = os.path.dirname(os.path.abspath(__file__))
            with open("config\config.json", "w") as config:
                json.dump(config_file, config, indent=4)
                
        csv_file, _ = QFileDialog.getOpenFileName(self, "Выберите CSV файлы", csv_path, "CSV файлы (*.csv)")
        self.name_dir.setText(csv_file)
        with open("config\config.json", "w") as config:
            config_file["path"]["default_csv_path"] = os.path.dirname(os.path.abspath(csv_file))
            json.dump(config_file, config, indent=4)
    
    #Метод вызывающий функцию сериализации и сохроняющий все данные в таблице
    def import_csv_passwords(self):
        if self.name_dir.text():
            passwords_csv = API.import_csv_passwords_api(self, self.name_dir.text())
            for value in passwords_csv:
                API.add_password_api(self, name=value["name_sit"], name_sit=value["url"], login=value["username"], mail=API.encryption_data_api(self, value["username"]), password=API.encryption_data_api(self, value["password"]))
            self.saved_table_passwords_csv.emit(True)
            self.accept()
            self.saved_table_passwords_csv.emit(False)
        else:
            self.name_dir.setStyleSheet("border: 1px solid red;")

#Класс диалогового окна экспорта csv файла
class DialogExportPasswords(Export_Ui_Dialog, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        try:
            self.buttonBox.accepted.disconnect()
        except TypeError:
            pass
        
        self.button_dir.clicked.connect(self.open_dialog_file)
        self.buttonBox.accepted.connect(self.export_csv_passwords)
    
    #Метод открытия окна файлового менеджера
    def open_dialog_file(self):
        csv_path = "C:/"
        
        with open("config\config.json", "r") as config:
            config_file = json.load(config)
        try:
            csv_path = config_file["path"]["default_csv_path"]
        except:
            config_file["path"]["default_csv_path"] = os.path.dirname(os.path.abspath(__file__))
            with open("config\config.json", "w") as config:
                json.dump(config_file, config, indent=4)
                 
        csv_file, _ = QFileDialog.getOpenFileName(self, "Выберите CSV файлы", csv_path, "CSV файлы (*.csv)")
        self.name_dir.setText(csv_file)
        with open("config\config.json", "w") as config:
            config_file["path"]["default_csv_path"] = os.path.dirname(os.path.abspath(csv_file))
            json.dump(config_file, config, indent=4)
    
    #Метод вызова функции экспорта
    def export_csv_passwords(self):
        API.export_csv_passwords_api(self, self.name_dir.text())
        self.accept()