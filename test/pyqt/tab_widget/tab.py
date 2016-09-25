#encoding: utf8
import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtCore import Qt

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    tabWidget = QtGui.QTabWidget()
    
    app.exec_()