# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'movies.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1077, 660)
        mainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableMovies = QtWidgets.QTableWidget(self.centralwidget)
        self.tableMovies.setGeometry(QtCore.QRect(30, 50, 711, 521))
        self.tableMovies.setObjectName("tableMovies")
        self.tableMovies.setColumnCount(0)
        self.tableMovies.setRowCount(0)
        self.btnTopRated = QtWidgets.QPushButton(self.centralwidget)
        self.btnTopRated.setGeometry(QtCore.QRect(830, 100, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.btnTopRated.setFont(font)
        self.btnTopRated.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.btnTopRated.setObjectName("btnTopRated")
        self.btnNowPlaying = QtWidgets.QPushButton(self.centralwidget)
        self.btnNowPlaying.setGeometry(QtCore.QRect(830, 170, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.btnNowPlaying.setFont(font)
        self.btnNowPlaying.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.btnNowPlaying.setObjectName("btnNowPlaying")
        self.btnComingSoon = QtWidgets.QPushButton(self.centralwidget)
        self.btnComingSoon.setGeometry(QtCore.QRect(830, 240, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.btnComingSoon.setFont(font)
        self.btnComingSoon.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.btnComingSoon.setObjectName("btnComingSoon")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(770, 370, 51, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.txtSearch = QtWidgets.QLineEdit(self.centralwidget)
        self.txtSearch.setGeometry(QtCore.QRect(830, 370, 191, 31))
        self.txtSearch.setObjectName("txtSearch")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(820, 330, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.btnSearch = QtWidgets.QPushButton(self.centralwidget)
        self.btnSearch.setGeometry(QtCore.QRect(830, 440, 191, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(193, 76, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(193, 76, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(193, 76, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(193, 76, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(193, 76, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(193, 76, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(193, 76, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(193, 76, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(193, 76, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        self.btnSearch.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.btnSearch.setFont(font)
        self.btnSearch.setAutoFillBackground(False)
        self.btnSearch.setStyleSheet("background-color: rgb(193, 76, 76);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imgs/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btnSearch.setIcon(icon)
        self.btnSearch.setObjectName("btnSearch")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1077, 26))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Movies From themoviedb"))
        self.btnTopRated.setText(_translate("mainWindow", "Top Rated"))
        self.btnNowPlaying.setText(_translate("mainWindow", "Now Playing"))
        self.btnComingSoon.setText(_translate("mainWindow", "Popular"))
        self.label.setText(_translate("mainWindow", "Name :"))
        self.label_2.setText(_translate("mainWindow", "Search By Movie Name"))
        self.btnSearch.setText(_translate("mainWindow", "Search"))
