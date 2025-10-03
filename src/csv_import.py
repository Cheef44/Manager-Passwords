import csv

#Класс импорта из csv файла
class PasswordCSV:
    def __init__(self, filedir:str):
        self.FILEDIR = filedir
    
    #Метод открытия csv файла   
    def open_csv_file(self):
        with open(self.FILEDIR, "r", newline="") as file_csv:
            reader_csv = csv.DictReader(file_csv)
            dict_csv = [value for value in reader_csv]
            return dict_csv
    
    #Сериализация данных из csv
    def processing_csv(self):
        dict_csv = self.open_csv_file()
        for key in range(len(dict_csv)):
            if not ("https" in dict_csv[key]["url"]):
                dict_csv[key]["name_sit"], dict_csv[key]["url"] = dict_csv[key]["url"], ""
            else:
                dict_csv[key]["name_sit"] = dict_csv[key]["url"][dict_csv[key]["url"].index("/")+2:]
        
        return dict_csv