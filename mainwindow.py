# -*- coding: utf-8 -*-
from PyQt4.QtGui import QMainWindow, QListWidgetItem, QMessageBox, QHeaderView
from ui_mainwindow import Ui_MainWindow
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt, pyqtSignal
import sys
import lab5

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.app = app
        self.btDo.clicked.connect(self.onBtnDoClick)
    def onBtnDoClick(self):
        self.teLog.clear()
        (result, log) = lab5.model()
        for logLine in log:
            self.teLog.append(logLine)
        self.lblResult.setText('Результат: %0.1f%% необслуженных клиентов' % (result*100))
