from PyQt6.QtCore import QAbstractTableModel, Qt
import chardet

#Класс модели таблицы паролей
class PasswordsTabel(QAbstractTableModel):
    def __init__(self, data, header):
        super().__init__()
        self._data = data
        self._header = header
    
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
            if type(self._data[index.row()][index.column()]) == bytes:
                if chardet.detect(self._data[index.row()][index.column()])["encoding"] != None:
                    return str(self._data[index.row()][index.column()].decode(chardet.detect(self._data[index.row()][index.column()])["encoding"]))
            else:
                return str(self._data[index.row()][index.column()])
        
        if role == Qt.ItemDataRole.TextAlignmentRole:
            return Qt.AlignmentFlag.AlignCenter
    
    #Функция возвращающая заголовки в таблицу
    def headerData(self, section, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return self._header[section]
            else:
                return str(section+1)