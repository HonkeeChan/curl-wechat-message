# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui
from qyolk import Ui_QYolk
from yolk import yolklib

class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_QYolk()
        self.ui.setupUi(self)
        # set the widths of the columns
        self.ui.treeList.setColumnWidth(0,200)
        self.ui.treeList.setColumnWidth(1,100)
    
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())