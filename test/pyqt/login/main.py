#encoding: utf8
import sys
from PyQt4 import QtCore, QtGui, uic


loginUIFile = "login.ui" # Enter file here.
mainUIFile = "main_window.ui"
Login_Ui_Dialog, QtBaseClass = uic.loadUiType(loginUIFile)
Main_Ui_MainWindow, QtBaseClass = uic.loadUiType(mainUIFile)


class LoginWindow(QtGui.QDialog, Login_Ui_Dialog):
    def __init__(self, mainWindow):
        QtGui.QMainWindow.__init__(self)
        Login_Ui_Dialog.__init__(self)
        self.setupUi(self)
        self.loginBtn.clicked.connect(self.OnLogin)
        self.mainWindow = mainWindow

    def OnLogin(self):
        print("username: %s" % self.usernameInput.text())
        print("password: %s" % self.passwordInput.text())
        self.hide()
        self.mainWindow.show()

# class GroupNameLabel(QtGui.QLabel):
#     def __init__(self):
#         QtGui.QLabel.__init__(self)

class MainWindow(QtGui.QMainWindow, Main_Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Main_Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.loginWindow = LoginWindow(self)
        self.hide()
        self.loginWindow.show()
        self.ShowQr()
        self.saveBtn.clicked.connect(self.OnSaveBtn)

    def ShowQr(self):
        self.pic = QtGui.QLabel(self)
        pixmap = QtGui.QPixmap("wxqr.png")
        self.pic.setPixmap(pixmap)
        self.pic.resize(pixmap.width(), pixmap.height())


    def ShowGroupName(self):
        groupArr = []
        groupArr = [("hello", "你好"), ("hi", "嗨"), \
            ("first", "第一"), ("hi", "嗨"), ("hi", "嗨"), \
            ("first", "第一"), ("hi", "嗨"), ("hi", "嗨"), \
            ("first", "第一"), ("hi", "嗨"), ("hi", "嗨"), \
            ("first", "第一"), ("hi", "嗨"), ("hi", "嗨")
        ]
        myform = QtGui.QTreeView()
        
        for group in groupArr:
            checkBox = QtGui.QCheckBox(group[1].decode("utf8"))
            myform.appendRow([checkBox])
        mygroupbox = QtGui.QGroupBox("")
        mygroupbox.setLayout(myform)
        self.groupNameScroll.setWidget(mygroupbox)

    def OnClickGroupLabel(self, label):
        print type(label)
        print label

    def OnSaveBtn(self):
        self.pic.hide()
        self.ShowGroupName()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mainWindow = MainWindow()
    # mainWindow.show()
    sys.exit(app.exec_())