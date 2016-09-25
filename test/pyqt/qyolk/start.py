# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt
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
        # generator which retuns list of installed packages
        packages = yolklib.Distributions()
        for pkg in packages.get_distributions('all'):

            a = QtGui.QTreeWidgetItem(self.ui.treeList)
            pk = str(pkg[0]).split(' ')
            if pkg[1]:
                status = 'Active'
            else:
                status = 'Not Active'
                a.setTextColor(0, QtGui.QColor(128, 128, 128))
                a.setTextColor(1, QtGui.QColor(128, 128, 128))
                a.setTextColor(2, QtGui.QColor(128, 128, 128))
            # a.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            # a.setCheckState(0, QtCore.Qt.Checked)
            a.setText(0, pk[0])
            a.setText(1, pk[1])
            a.setText(2, status)
            a.setText(3, status)
    
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())