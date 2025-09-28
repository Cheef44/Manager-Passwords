from PyQt6.QtCore import QAbstractTableModel, Qt, QModelIndex
import chardet
from src.api import API
import logging
#logging.basicConfig(level=logging.DEBUG)

#Класс модели таблицы паролей
class PasswordsTabel(QAbstractTableModel):
    def __init__(self, data, header):
        super().__init__()
        self._data = self.data_processing([list(item) for item in data])
        self._header = header
        
    #Обработка данных для быстрой подгрузки
    def data_processing(self, data:list):
        for key in range(len(data)):
            values = []
            for value in data[key]:
                if type(value) != bytes:
                    values.append(value)
                else:
                    try:
                        values.append(API.decryption_data_api(self, value))
                    except TypeError:
                        values.append("")
                if len(values) == len(data[key]):
                    data[key] = values
        
        return data

    #Обновление id данных
    def update_num_id(self, data:list):
        for key in range(len(data)):
            data[key][0] = key+1
        
        return data
    
    #Функция возвращающая количество строк
    def rowCount(self, parent = None):
        return len(self._data)
    
    #Функция возвращающая количество столбцов
    def columnCount(self, parent = None):
        return len(self._header)
    
    #Функция возвращающая данные в таблицу
    def data(self, index, role = Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return None
        
        if role == Qt.ItemDataRole.DisplayRole:
            if not self._data:
                return ""
            if type(self._data[index.row()][index.column()]) == bytes:
                try:
                    return API.decryption_data_api(self, self._data[index.row()][index.column()])
                except TypeError:
                    return ""
            else:
                return self._data[index.row()][index.column()]
        
        if role == Qt.ItemDataRole.TextAlignmentRole:
            return Qt.AlignmentFlag.AlignCenter
    
    #Метод редактирования таблицы
    def setData(self, index, value, role=Qt.ItemDataRole.EditRole):
        if role == Qt.ItemDataRole.EditRole:
            self._data[index.row()][index.column()] = value
            self.dataChanged.emit(index, index, [Qt.ItemDataRole.DisplayRole])
            if type(self._data[index.row()][-1]) != bytes:
                self._data[index.row()][-1] = API.encryption_data_api(self, self._data[index.row()][-1])
            API.uptade_password_api(self, id=self._data[index.row()][0], name=self._data[index.row()][1], name_sit=self._data[index.row()][2], login=self._data[index.row()][3], mail=self._data[index.row()][4], password=self._data[index.row()][-1])
            return True
        return False
    
    #Метод выдающий флаги ячейкам
    def flags(self, index):
        if index.column() == 0:
            return Qt.ItemFlag.NoItemFlags
        return Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsEditable
    
    #Функция возвращающая заголовки в таблицу
    def headerData(self, section, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return self._header[section]
            else:
                return str(section+1)
    
    #Метод удаления строк
    def removeRow(self, row, parent=QModelIndex()):
        self.beginRemoveRows(parent, row, row)
        del self._data[row]
        self._data = self.update_num_id(self._data)
        self.endRemoveRows()
        return True