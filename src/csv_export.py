import csv
from src.decryption import Decryption
from src.db import DataBase


#Класс экспорта паролей в csv файл
class PasswordCSVExport:
    def __init__(self, filedir):
        self.FILEDIR = filedir
    
    #Функция записи паролей в csv файл
    def write_file_csv(self):
        with open(self.FILEDIR, "w", newline="") as file_csv:
            render_csv_file = csv.writer(file_csv)
            render_csv_file.writerows(self.data_preparation())
        return True
    
    #Функция подготовки данных для экспорта
    def data_preparation(self):
        data = []
        for rows in DataBase().retrieve_data_passwords():
            row = []
            for columns in rows:
                if columns == b'':
                    columns = ""
                if type(columns) == bytes:
                    columns = Decryption(columns).decryption()
                row.append(columns)
                
            data.append(row)
        return data
                