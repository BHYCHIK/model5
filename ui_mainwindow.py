# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Wed Nov 20 02:22:47 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(663, 422)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btDo = QtGui.QPushButton(self.centralwidget)
        self.btDo.setGeometry(QtCore.QRect(20, 320, 151, 51))
        self.btDo.setObjectName(_fromUtf8("btDo"))
        self.lblResult = QtGui.QLabel(self.centralwidget)
        self.lblResult.setGeometry(QtCore.QRect(190, 330, 461, 31))
        self.lblResult.setObjectName(_fromUtf8("lblResult"))
        self.teLog = QtGui.QTextEdit(self.centralwidget)
        self.teLog.setGeometry(QtCore.QRect(10, 20, 641, 281))
        self.teLog.setObjectName(_fromUtf8("teLog"))
        self.lblLog = QtGui.QLabel(self.centralwidget)
        self.lblLog.setGeometry(QtCore.QRect(20, 0, 141, 17))
        self.lblLog.setObjectName(_fromUtf8("lblLog"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 663, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Моделирование 5", None, QtGui.QApplication.UnicodeUTF8))
        self.btDo.setText(QtGui.QApplication.translate("MainWindow", "Смоделировать", None, QtGui.QApplication.UnicodeUTF8))
        self.lblResult.setText(QtGui.QApplication.translate("MainWindow", "Результат: ", None, QtGui.QApplication.UnicodeUTF8))
        self.lblLog.setText(QtGui.QApplication.translate("MainWindow", "Лог моделирования", None, QtGui.QApplication.UnicodeUTF8))

