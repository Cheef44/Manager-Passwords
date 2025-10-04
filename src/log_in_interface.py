# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'log_in.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_log_in(object):
    def setupUi(self, log_in):
        if not log_in.objectName():
            log_in.setObjectName(u"log_in")
        log_in.setEnabled(True)
        log_in.resize(494, 617)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(log_in.sizePolicy().hasHeightForWidth())
        log_in.setSizePolicy(sizePolicy)
        log_in.setMinimumSize(QSize(494, 617))
        log_in.setMaximumSize(QSize(494, 617))
        log_in.setAutoFillBackground(False)
        log_in.setStyleSheet(u"")
        self.centralwidget = QWidget(log_in)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"font-size: 20px")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(50, 0, 50, 0)
        self.input = QFrame(self.centralwidget)
        self.input.setObjectName(u"input")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.input.sizePolicy().hasHeightForWidth())
        self.input.setSizePolicy(sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.input)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.login = QLabel(self.input)
        self.login.setObjectName(u"login")
        sizePolicy.setHeightForWidth(self.login.sizePolicy().hasHeightForWidth())
        self.login.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.login)

        self.login_input = QLineEdit(self.input)
        self.login_input.setObjectName(u"login_input")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.login_input.sizePolicy().hasHeightForWidth())
        self.login_input.setSizePolicy(sizePolicy2)
        self.login_input.setMaximumSize(QSize(16777215, 40))
        self.login_input.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.login_input)

        self.password = QLabel(self.input)
        self.password.setObjectName(u"password")
        sizePolicy.setHeightForWidth(self.password.sizePolicy().hasHeightForWidth())
        self.password.setSizePolicy(sizePolicy)
        self.password.setMargin(0)

        self.verticalLayout.addWidget(self.password)

        self.password_input_1 = QLineEdit(self.input)
        self.password_input_1.setObjectName(u"password_input_1")
        self.password_input_1.setMaximumSize(QSize(16777215, 40))
        self.password_input_1.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout.addWidget(self.password_input_1)

        self.password_input_2 = QLineEdit(self.input)
        self.password_input_2.setObjectName(u"password_input_2")
        self.password_input_2.setEnabled(True)
        self.password_input_2.setMaximumSize(QSize(16777215, 40))
        self.password_input_2.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout.addWidget(self.password_input_2)


        self.verticalLayout_2.addWidget(self.input)

        self.button_log_in = QFrame(self.centralwidget)
        self.button_log_in.setObjectName(u"button_log_in")
        sizePolicy2.setHeightForWidth(self.button_log_in.sizePolicy().hasHeightForWidth())
        self.button_log_in.setSizePolicy(sizePolicy2)
        self.button_log_in.setMaximumSize(QSize(16777215, 300))
        self.button_log_in.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.button_log_in)
        self.horizontalLayout.setSpacing(50)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(20, 0, 20, 200)
        self.log_in_2 = QPushButton(self.button_log_in)
        self.log_in_2.setObjectName(u"log_in_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.log_in_2.sizePolicy().hasHeightForWidth())
        self.log_in_2.setSizePolicy(sizePolicy3)
        self.log_in_2.setMaximumSize(QSize(16777215, 50))
        self.log_in_2.setAcceptDrops(False)
        self.log_in_2.setStyleSheet(u"")
        self.log_in_2.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.log_in_2)

        self.registration = QPushButton(self.button_log_in)
        self.registration.setObjectName(u"registration")
        sizePolicy3.setHeightForWidth(self.registration.sizePolicy().hasHeightForWidth())
        self.registration.setSizePolicy(sizePolicy3)
        self.registration.setMaximumSize(QSize(16777215, 50))
        self.registration.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.registration)


        self.verticalLayout_2.addWidget(self.button_log_in)

        log_in.setCentralWidget(self.centralwidget)

        self.retranslateUi(log_in)

        QMetaObject.connectSlotsByName(log_in)
    # setupUi

    def retranslateUi(self, log_in):
        log_in.setWindowTitle(QCoreApplication.translate("log_in", u"Manager Password", None))
#if QT_CONFIG(whatsthis)
        self.centralwidget.setWhatsThis(QCoreApplication.translate("log_in", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.login.setText(QCoreApplication.translate("log_in", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.password.setText(QCoreApplication.translate("log_in", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.log_in_2.setText(QCoreApplication.translate("log_in", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.registration.setText(QCoreApplication.translate("log_in", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
    # retranslateUi

