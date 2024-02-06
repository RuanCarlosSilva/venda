# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cliente.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 791, 571))
        self.frame.setStyleSheet(u"background-color: #ffffff")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.nome_txt = QLineEdit(self.frame)
        self.nome_txt.setObjectName(u"nome_txt")
        self.nome_txt.setGeometry(QRect(70, 110, 301, 22))
        self.cpf_txt = QLineEdit(self.frame)
        self.cpf_txt.setObjectName(u"cpf_txt")
        self.cpf_txt.setGeometry(QRect(70, 160, 301, 22))
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 110, 49, 16))
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 160, 49, 16))
        self.label_2.setFont(font)
        self.btn_cadastrar = QPushButton(self.frame)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setGeometry(QRect(410, 110, 75, 24))
        self.btn_cadastrar.setStyleSheet(u"background-color: rgb(216, 216, 216);")
        self.btn_pesquisar = QPushButton(self.frame)
        self.btn_pesquisar.setObjectName(u"btn_pesquisar")
        self.btn_pesquisar.setGeometry(QRect(410, 160, 75, 24))
        self.btn_pesquisar.setStyleSheet(u"background-color: rgb(216, 216, 216);")
        self.btn_editar = QPushButton(self.frame)
        self.btn_editar.setObjectName(u"btn_editar")
        self.btn_editar.setGeometry(QRect(410, 210, 75, 24))
        self.btn_editar.setStyleSheet(u"background-color: rgb(216, 216, 216);")
        self.btn_excluir = QPushButton(self.frame)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setGeometry(QRect(410, 270, 75, 24))
        self.btn_excluir.setStyleSheet(u"background-color: rgb(216, 216, 216);")
        self.tableWidget = QTableWidget(self.frame)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(60, 260, 321, 251))
        font1 = QFont()
        font1.setBold(False)
        self.tableWidget.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"CPF:", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR", None))
        self.btn_pesquisar.setText(QCoreApplication.translate("MainWindow", u"PESQUISAR", None))
        self.btn_editar.setText(QCoreApplication.translate("MainWindow", u"EDITAR", None))
        self.btn_excluir.setText(QCoreApplication.translate("MainWindow", u"EXCLUIR", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"CPF", None));
    # retranslateUi

