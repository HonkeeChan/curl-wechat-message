#encoding: utf8
import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtCore import Qt
from wxbot import *
from loading_modal_dialog import LoadingDialog
from tab import MessageTableWidget
import logging
import threading
import os
import time

os.environ["REQUESTS_CA_BUNDLE"] = "certifi/cacert.pem"

logger = logging.getLogger("wechat_message")
logger.setLevel(logging.DEBUG)
# 创建一个handler，用于写入日志文件
fh = logging.FileHandler("wechat_message.log")
fh.setLevel(logging.DEBUG)

# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# 定义handler的输出格式
formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 给logger添加handler
logger.addHandler(fh)
logger.addHandler(ch)

groupArr = []
# groupArr = [
#     {"id": "chenhongjian1", "name": "陈洪健1"},
#     {"id": "chenhongjian2", "name": "陈洪健2"},
#     {"id": "chenhongjian3", "name": "陈洪健3"},
#     {"id": "chenhongjian4", "name": "陈洪健4"},
#     {"id": "chenhongjian5", "name": "陈洪健5"},
#     {"id": "chenhongjian6", "name": "陈洪健6"},
#     {"id": "chenhongjian7", "name": "陈洪健7"},
#     {"id": "chenhongjian8", "name": "陈洪健8"},
#     {"id": "chenhongjian9", "name": "陈洪健9"},
# ]
selectGroupMap = {}
# selectGroupMap["chenhongjian1"] = {
#     "name": "陈洪健1", 
#     "config":{
#         "id": 1
#     }
# }
# selectGroupMap["chenhongjian2"] = {
#     "name": "陈洪健2", 
#     "config":{
#         "id": 2
#     }
# }
messageArr = []
messageLock = threading.Lock()

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
        self.mainWindow.ShowQr()

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
        self.saveBtn.clicked.connect(self.OnSaveBtn)
        self.preSelectIdx = -1
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.CheckLoadingStatus)

        self.messageRefreshTimer = QtCore.QTimer()
        self.messageRefreshTimer.timeout.connect(self.RefreshMessageTab)

    def ShowQr(self):
        # self.pic = QtGui.QLabel(self)
        # pixmap = QtGui.QPixmap("wxqr.png")
        # self.pic.setPixmap(pixmap)
        # self.pic.resize(pixmap.width(), pixmap.height())
        logger.debug("show qr code")
        self.loadingDialog = LoadingDialog()
        if os.path.exists("temp/wxqr.png"):
            logger.debug("qr code exist")
            self.loadingDialog.ChangeImage("temp/wxqr.png")
            self.timer.start(1000)
            self.loadingDialog.exec_()
        else:
            logger.error("不能获取二维码")
            # 请检查你的网络
            msgBox = QtGui.QMessageBox()
            msgBox.setText(u"请检查你的网络")
            msgBox.exec_()
            self.close()


    def CheckLoadingStatus(self):
        # logger.debug("check loading scatus")
        if bot.qrScaned :
            logger.debug("qr code scaned")
            self.loadingDialog.ChangeImage("loading.gif")
        if bot.contactLoaded:
            self.contactLoaded = True
            logger.debug("contact loaded")
            self.timer.stop()
            self.loadingDialog.done(0)
            self.LoadFinish()
            

    def ShowGroupName(self):
        logger.debug("show group name")
        self.listWidget = QtGui.QListWidget()
        for group in groupArr:
            item = QtGui.QListWidgetItem(group["name"], self.listWidget)
            item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            item.setCheckState(Qt.Unchecked)
            self.listWidget.addItem(item)
            
        self.listWidget.currentRowChanged.connect(self.OnListWidgetRowChanged)
        self.listWidget.itemClicked.connect(self.OnListWidgetItemClicked)
        self.groupNameScroll.setWidget(self.listWidget)

    def SaveConfig(self):
        if self.preSelectIdx != -1 and self.preSelectIdx < len(groupArr):
            logger.info("save config")
            if selectGroupMap.has_key(groupArr[self.preSelectIdx]["id"]):
                groupId = groupArr[self.preSelectIdx]["id"]
                config = selectGroupMap[groupId]["config"]
                config["id"] = self.configId.text()

    def InitMessageTab(self):
        logger.debug("init message tab")
        self.gid2messageTable = {}
        for k, v in selectGroupMap.items():
            logger.debug("init group %s tab", v["name"].encode("utf8"))
            table = MessageTableWidget()
            table.setHeaderName([u"用户名", u"群聊名", u"消息", u"时间"])
            self.gid2messageTable[k] = table
            self.messageTab.addTab(table, v["name"])
        logger.debug("start refresh message per 500ms")
        self.messageRefreshTimer.start(500)

    def RefreshMessageTab(self):
        # logger.debug("refressing message")
        if len(messageArr) > 0:

            messageLock.acquire()
            msg = messageArr[0]
            messageArr.remove(msg)
            messageLock.release()
            if self.gid2messageTable.has_key(msg["FromGroupId"]):
                logger.debug("add data to tab %s", msg["FromGroupName"])
                logger.debug("refresh message tab, msg: %s", msg)
                table = self.gid2messageTable[msg["FromGroupId"]]
                rowData = [
                    [
                        msg["FromUserNickName"], 
                        msg["FromGroupName"],
                        msg["MsgContent"], 
                        msg["Time"]
                    ]
                ]
                logger.debug("row data: %s", rowData)
                table.appendRows(rowData)
            # msg = {
            #         "FromUserName": fromUsername,
            #         "FromUserNickName": fromUserNickname,
            #         "FromGroupId": fromGroupId,
            #         "FromGroupName": fromGroupName,
            #         "MsgContent": content
            #         "Time": time.strftime("%y-%m-%d %H:%M:%S")
            #     }
        
        

    def LoadFinish(self):
        # self.pic.hide()
        self.ShowGroupName()
        # self.InitMessageTab()



    def OnListWidgetRowChanged(self, idx):
        self.SaveConfig()
        self.preSelectIdx = idx
        if selectGroupMap.has_key(groupArr[idx]["id"]):
            groupId = groupArr[self.preSelectIdx]["id"]
            config = selectGroupMap[groupId]["config"]
            if config.has_key("id"):
                self.configId.setText(config["id"])
        else:
            self.configId.setText("")

    def OnListWidgetItemClicked(self, item):
        # 处理勾选的列表
        groupCnt = self.listWidget.count()
        for i in range(groupCnt):
            if self.listWidget.item(i).checkState() == Qt.Checked:
                if not selectGroupMap.has_key(groupArr[i]["id"]):
                    selectGroupMap[groupArr[i]["id"]] = {}
                    selectGroupMap[groupArr[i]["id"]]["name"] = groupArr[i]["name"]
                    config = selectGroupMap[groupArr[i]["id"]]["config"] = {}

        logger.info("select group map: %s", selectGroupMap)

    
    def OnSaveBtn(self):
        self.InitMessageTab()


class MyWXBot(WXBot):
    def handle_msg_all(self, msg):
        # print msg
        if msg['msg_type_id'] == 3 and msg['content']['type'] == 0:
            """
            {
                'content': {
                    'data': u'aa', 
                    'desc': u'aa', 
                    'type': 0, 
                    'user': {
                        'id': u'@10ac71277ce6f3c76763a1302830361c2d8215d9a95441d3742cfc4391c82b8d',  //from user id
                        'name': u'\u81ea\u5df1\u597d\u53e5'
                    }, 
                    'detail': [{'type': 'str', 'value': u'aa'}]
                }, 
                'msg_id': u'2185443169392681243', 
                'msg_type_id': 3, 
                'to_user_id': u'@9f6b3f26463c348f0b10bf6cc61a031a',  //my id
                'user': {
                    'id': u'@@9f41ee170abc31fd5f17c1c0c4f2bde3adf49b81bfa19bbdfae900547242f627', //from group user id
                    'name': u'\u6d4b\u8bd5\u7528'
                }
            }
            """
            groupUsername = msg['user']['id']
            if(selectGroupMap.has_key(groupUsername)):
                fromUsername = msg["content"]["user"]["id"]
                fromUserNickname = msg["content"]["user"]["name"]
                fromGroupId = msg["user"]["id"]
                fromGroupName = msg["user"]["name"]
                sendMsg = u"收到你在 " +fromGroupName + u" 上发的消息 " + \
                        msg['content']['data']
                msg = {
                    "FromUserName": fromUsername,
                    "FromUserNickName": fromUserNickname,
                    "FromGroupId": fromGroupId,
                    "FromGroupName": fromGroupName,
                    "MsgContent": msg['content']['data'],
                    "Time": time.strftime("%y-%m-%d %H:%M:%S")
                }
                
                messageLock.acquire()
                messageArr.append(msg)
                messageLock.release()
                self.send_msg_by_uid(sendMsg, fromUsername)
                self.send_msg_by_uid(sendMsg, fromGroupId)
        

    def get_contact(self):
        print 'MyWxBot get contact'
        WXBot.get_contact(self)
        for group in self.group_list:
            groupArr.append({"id": group["UserName"], "name": group["NickName"]})


def mybot():
    global bot
    global botThreadRuning
    botThreadRuning = True
    bot = MyWXBot()
    bot.DEBUG = False
    bot.conf['qr'] = 'png'
    bot.run()
    botThreadRuning = False


if __name__ == "__main__":
    if os.path.exists("temp/wxqr.png"):
        os.remove("temp/wxqr.png")
        logger.debug("clear wx qr code")
    wxBotThread = threading.Thread(target = mybot)
    wxBotThread.start()

    app = QtGui.QApplication(sys.argv)
    mainWindow = MainWindow()
    app.exec_()
    bot.run_flag = False