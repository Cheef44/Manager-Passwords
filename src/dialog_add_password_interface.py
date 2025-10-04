# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_add_password.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Add_password(object):
    def setupUi(self, Add_password):
        if not Add_password.objectName():
            Add_password.setObjectName(u"Add_password")
        Add_password.setEnabled(True)
        Add_password.resize(483, 194)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Add_password.sizePolicy().hasHeightForWidth())
        Add_password.setSizePolicy(sizePolicy)
        Add_password.setMaximumSize(QSize(483, 194))
        Add_password.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        Add_password.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        Add_password.setAcceptDrops(False)
        Add_password.setAutoFillBackground(False)
        Add_password.setInputMethodHints(Qt.InputMethodHint.ImhPreferUppercase)
        Add_password.setSizeGripEnabled(False)
        Add_password.setModal(False)
        self.verticalLayout_2 = QVBoxLayout(Add_password)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.name = QHBoxLayout()
        self.name.setObjectName(u"name")
        self.name_label = QLabel(Add_password)
        self.name_label.setObjectName(u"name_label")

        self.name.addWidget(self.name_label)

        self.name_input = QLineEdit(Add_password)
        self.name_input.setObjectName(u"name_input")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.name_input.sizePolicy().hasHeightForWidth())
        self.name_input.setSizePolicy(sizePolicy1)
        self.name_input.setMinimumSize(QSize(390, 0))

        self.name.addWidget(self.name_input)


        self.verticalLayout.addLayout(self.name)

        self.site = QHBoxLayout()
        self.site.setSpacing(6)
        self.site.setObjectName(u"site")
        self.sit_label = QLabel(Add_password)
        self.sit_label.setObjectName(u"sit_label")

        self.site.addWidget(self.sit_label)

        self.sit_input = QLineEdit(Add_password)
        self.sit_input.setObjectName(u"sit_input")
        sizePolicy1.setHeightForWidth(self.sit_input.sizePolicy().hasHeightForWidth())
        self.sit_input.setSizePolicy(sizePolicy1)
        self.sit_input.setMinimumSize(QSize(390, 0))

        self.site.addWidget(self.sit_input)


        self.verticalLayout.addLayout(self.site)

        self.login = QHBoxLayout()
        self.login.setObjectName(u"login")
        self.login_label = QLabel(Add_password)
        self.login_label.setObjectName(u"login_label")

        self.login.addWidget(self.login_label)

        self.login_input = QLineEdit(Add_password)
        self.login_input.setObjectName(u"login_input")
        sizePolicy1.setHeightForWidth(self.login_input.sizePolicy().hasHeightForWidth())
        self.login_input.setSizePolicy(sizePolicy1)
        self.login_input.setMinimumSize(QSize(390, 0))

        self.login.addWidget(self.login_input)


        self.verticalLayout.addLayout(self.login)

        self.email = QHBoxLayout()
        self.email.setSpacing(6)
        self.email.setObjectName(u"email")
        self.email_label = QLabel(Add_password)
        self.email_label.setObjectName(u"email_label")

        self.email.addWidget(self.email_label)

        self.email_input = QLineEdit(Add_password)
        self.email_input.setObjectName(u"email_input")
        sizePolicy1.setHeightForWidth(self.email_input.sizePolicy().hasHeightForWidth())
        self.email_input.setSizePolicy(sizePolicy1)
        self.email_input.setMinimumSize(QSize(390, 0))

        self.email.addWidget(self.email_input)


        self.verticalLayout.addLayout(self.email)

        self.password = QHBoxLayout()
        self.password.setObjectName(u"password")
        self.password_label = QLabel(Add_password)
        self.password_label.setObjectName(u"password_label")

        self.password.addWidget(self.password_label)

        self.password_input = QLineEdit(Add_password)
        self.password_input.setObjectName(u"password_input")
        sizePolicy1.setHeightForWidth(self.password_input.sizePolicy().hasHeightForWidth())
        self.password_input.setSizePolicy(sizePolicy1)
        self.password_input.setMinimumSize(QSize(390, 0))

        self.password.addWidget(self.password_input)


        self.verticalLayout.addLayout(self.password)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.buttonBox = QDialogButtonBox(Add_password)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(Add_password)
        self.buttonBox.accepted.connect(Add_password.accept)
        self.buttonBox.rejected.connect(Add_password.reject)

        QMetaObject.connectSlotsByName(Add_password)
    # setupUi

    def retranslateUi(self, Add_password):
        Add_password.setWindowTitle(QCoreApplication.translate("Add_password", u"Add Password", None))
#if QT_CONFIG(tooltip)
        Add_password.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        Add_password.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        Add_password.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.name_label.setText(QCoreApplication.translate("Add_password", u"\u0418\u043c\u044f \u0437\u0430\u043f\u0438\u0441\u0438", None))
        self.sit_label.setText(QCoreApplication.translate("Add_password", u"\u0421\u0430\u0439\u0442", None))
        self.login_label.setText(QCoreApplication.translate("Add_password", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.email_label.setText(QCoreApplication.translate("Add_password", u"\u041f\u043e\u0447\u0442\u0430", None))
        self.password_label.setText(QCoreApplication.translate("Add_password", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
    # retranslateUi

