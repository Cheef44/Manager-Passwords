from PyQt6.QtWidgets import QWidget, QMenu
from PyQt6.QtGui import QCursor

#Класс контекстного меню
class ContextMenu(QWidget):
    def __init__(self, menu: dict):
        super().__init__()
        self.menu = menu
        self.context_menu = QMenu(self)
        for element, func in self.menu.items():
            self.context_menu.addAction(element, func)
        self.context_menu.exec(QCursor.pos())