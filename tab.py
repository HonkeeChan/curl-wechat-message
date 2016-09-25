#encoding: utf8
import sys
from PyQt4.QtCore import QString
from PyQt4.QtGui import QTableWidgetItem
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtCore import Qt

class MessageTableWidget(QtGui.QTableWidget):
    def __init__(self):
        QtGui.QTableWidget.__init__(self)

    def setHeaderName(self, headerNames):
        qsList = QtCore.QStringList()
        headerLen = len(headerNames)
        self.setColumnCount(headerLen)
        for name in headerNames:
            qsList.append(QString(name))
        self.setHorizontalHeaderLabels(qsList)

    def appendRows(self, rows):

        for r in rows:
            rowPos = self.rowCount()
            self.insertRow(rowPos)
            rLen = len(r)
            if rLen > self.columnCount():
                rLen = self.columnCount()
            for i in range(rLen):
                self.setItem(rowPos, i, QTableWidgetItem(r[i]))

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    tabWidget = QtGui.QTabWidget()
    tabelWidget = QtGui.QTableWidget()
    rowPosition = tabelWidget.rowCount()
    print 'row cnt', rowPosition
    tabelWidget.setColumnCount(3)
    qsList = QtCore.QStringList()
    qsList.append(QtCore.QString("a"))
    qsList.append(QtCore.QString("b"))
    qsList.append(QtCore.QString("c"))

    tabelWidget.setHorizontalHeaderLabels(qsList)
    tabelWidget.insertRow(rowPosition)
    tabelWidget.setItem(rowPosition, 0, QtGui.QTableWidgetItem("text1"))
    tabelWidget.setItem(rowPosition, 1, QtGui.QTableWidgetItem("text2"))
    tabelWidget.setItem(rowPosition, 2, QtGui.QTableWidgetItem("text3"))
    tabWidget.addTab(tabelWidget, "tab1")

    tabelWidget1 = MessageTableWidget()
    headerNames = [u"text1", u"text2", u"text3"]
    rowsData = [
        [u"a", u"b", u"c", u"d"],
        [u"e", u"f", u"h"]
    ]
    tabelWidget1.setHeaderName(headerNames)
    tabelWidget1.appendRows(rowsData)
    tabWidget.addTab(tabelWidget1, "tab2")
    tabWidget.show()
    app.exec_()