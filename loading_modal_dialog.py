#encoding: utf8
import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtCore import Qt

class LoadingDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.pic = QtGui.QLabel(self)
        self.ChangeImage("loading.gif")


    def ChangeImage(self, path):
        pixmap = QtGui.QPixmap(path)
        self.pic.setPixmap(pixmap)
        self.pic.resize(pixmap.width(), pixmap.height())

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    d = LoadingDialog()
    d.show()
    app.exec_()

