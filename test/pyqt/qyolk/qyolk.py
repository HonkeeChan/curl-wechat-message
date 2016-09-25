# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qyolk.ui'
#
# Created: Tue May  8 18:16:12 2007
#      by: PyQt4 UI code generator 4.1.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_QYolk(object):
    def setupUi(self, QYolk):
        QYolk.setObjectName("QYolk")
        QYolk.setWindowModality(QtCore.Qt.NonModal)
        QYolk.resize(QtCore.QSize(QtCore.QRect(0,0,501,420).size()).expandedTo(QYolk.minimumSizeHint()))
        QYolk.setWindowIcon(QtGui.QIcon("waaaht-7.png"))

        self.centralwidget = QtGui.QWidget(QYolk)
        self.centralwidget.setObjectName("centralwidget")

        self.gridlayout = QtGui.QGridLayout(self.centralwidget)
        self.gridlayout.setMargin(9)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")

        self.InfoLabel = QtGui.QLabel(self.centralwidget)
        self.InfoLabel.setObjectName("InfoLabel")
        self.gridlayout.addWidget(self.InfoLabel,0,0,1,1)

        self.treeList = QtGui.QTreeWidget(self.centralwidget)
        self.treeList.setObjectName("treeList")
        self.gridlayout.addWidget(self.treeList,1,0,1,1)
        QYolk.setCentralWidget(self.centralwidget)

        self.statusbar = QtGui.QStatusBar(QYolk)
        self.statusbar.setObjectName("statusbar")
        QYolk.setStatusBar(self.statusbar)

        self.menubar = QtGui.QMenuBar(QYolk)
        self.menubar.setGeometry(QtCore.QRect(0,0,501,26))
        self.menubar.setObjectName("menubar")
        QYolk.setMenuBar(self.menubar)

        self.retranslateUi(QYolk)
        QtCore.QMetaObject.connectSlotsByName(QYolk)

    def retranslateUi(self, QYolk):
        QYolk.setWindowTitle(QtGui.QApplication.translate("QYolk", "QYolk", None, QtGui.QApplication.UnicodeUTF8))
        self.InfoLabel.setText(QtGui.QApplication.translate("QYolk", "<b>QYolk</b>: Browsing all installed cheeseshop packages", None, QtGui.QApplication.UnicodeUTF8))
        self.treeList.headerItem().setText(0,QtGui.QApplication.translate("QYolk", "Package Name", None, QtGui.QApplication.UnicodeUTF8))
        self.treeList.headerItem().setText(1,QtGui.QApplication.translate("QYolk", "Version", None, QtGui.QApplication.UnicodeUTF8))
        self.treeList.headerItem().setText(2,QtGui.QApplication.translate("QYolk", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.treeList.headerItem().setText(3,QtGui.QApplication.translate("QYolk", "Status", None, QtGui.QApplication.UnicodeUTF8))

