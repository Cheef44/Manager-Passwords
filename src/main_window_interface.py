# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 705)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.header = QHBoxLayout()
        self.header.setObjectName(u"header")
        self.add_data = QPushButton(self.centralwidget)
        self.add_data.setObjectName(u"add_data")

        self.header.addWidget(self.add_data)

        self.csv_import = QPushButton(self.centralwidget)
        self.csv_import.setObjectName(u"csv_import")

        self.header.addWidget(self.csv_import)

        self.search = QLineEdit(self.centralwidget)
        self.search.setObjectName(u"search")

        self.header.addWidget(self.search)

        self.user_name = QLabel(self.centralwidget)
        self.user_name.setObjectName(u"user_name")

        self.header.addWidget(self.user_name)


        self.verticalLayout_2.addLayout(self.header)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.list_passwords = QLabel(self.centralwidget)
        self.list_passwords.setObjectName(u"list_passwords")

        self.verticalLayout.addWidget(self.list_passwords)

        self.table_passwords = QTableView(self.centralwidget)
        self.table_passwords.setObjectName(u"table_passwords")
        self.table_passwords.setAcceptDrops(False)
        self.table_passwords.setAlternatingRowColors(False)

        self.verticalLayout.addWidget(self.table_passwords)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.add_data.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.csv_import.setText(QCoreApplication.translate("MainWindow", u" \u2193", None))
        self.user_name.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.list_passwords.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u043f\u0430\u0440\u043e\u043b\u0435\u0439", None))
    # retranslateUi

