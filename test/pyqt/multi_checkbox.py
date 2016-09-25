import sys
from PyQt4 import QtGui, QtCore

app = QtGui.QApplication(sys.argv)
widget = QtGui.QWidget()

widget.setGeometry(200, 100, 400, 300)
widget.setWindowTitle('PyQt Application')

foods = ['Ayam Bakar','Lalapan','Soto','Sate'];
len = len(foods)
cb = []
a = 0

for i in foods:
    cb.append(QtGui.QCheckBox(i, widget))
    a = a + 1;
    
a = 0
for i in foods:
    cb[a].move(10, 20*a)
    a = a + 1

def hello():
    for i in range(0,len):
        if cb[i].isChecked():
            widget.setWindowTitle(foods[i])
            break;
        else:
            widget.setWindowTitle('None')
            
for i in range(0,len):
    widget.connect(cb[i], QtCore.SIGNAL('stateChanged(int)'), hello)

widget.show()
sys.exit(app.exec_())