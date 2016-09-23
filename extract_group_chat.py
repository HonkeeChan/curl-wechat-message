#!/usr/bin/env python
# coding: utf-8

from wxbot import *
from Tkinter import *
import threading
import time

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
            if(usernameMap.has_key(groupUsername)):
                if(usernameMap[groupUsername][1].get() == True):
                    fromUsername = msg["content"]["user"]["id"]
                    fromUserNickname = msg["content"]["user"]["name"]
                    fromGroupId = msg["user"]["id"]
                    fromGroupName = msg["user"]["name"]
                    sendMsg = "收到你在 " +fromGroupName.encode("utf8")+" 上发的消息 " + msg['content']['data'].encode("utf8") 
                    self.send_msg_by_uid(sendMsg, fromUsername)
                    self.send_msg_by_uid(sendMsg, fromGroupId)
        

    def get_contact(self):
        print 'MyWxBot get contact'
        WXBot.get_contact(self)
        for group in self.group_list:
            usernameMap[group['UserName']] = (group['NickName'], None)
        
'''
    def schedule(self):
        self.send_msg(u'张三', u'测试')
        time.sleep(1)
'''



def main():
    bot = MyWXBot()
    bot.DEBUG = False
    bot.conf['qr'] = 'png'
    bot.run()

def printItem():
    pass
    # for k, v in usernameMap.items():
    #     print 'k: ',k , 'v: ', v

def addMenu():
    try:
        # print 'create new menu'
        for k, v in usernameMap.items():
            nickname = usernameMap[k][0]
            if usernameMap[k][1] == None:
                var = BooleanVar()
            else:
                var = usernameMap[k][1]
            usernameMap[k] = (nickname, var)

        menubar = Menu(root)
        filemenu = Menu(menubar,tearoff = 0)
        for k, v in usernameMap.items():
            #绑定变量与回调函数
            filemenu.add_checkbutton(label = (usernameMap[k][0]).encode('utf8'),command = printItem,variable = usernameMap[k][1])
        #将menubar的menu属性指定为filemenu，即filemenu为menubar的下拉菜单
        menubar.add_cascade(label = '监听群名',menu = filemenu)
        root['menu'] = menubar
        root.after(10000, addMenu)
    except Exception, e:
        print 'exception, ', e

def gui():
    time.sleep(10)
    global root
    root = Tk()
    addMenu()
    root.mainloop()

if __name__ == '__main__':
    global usernameMap
    usernameMap = dict()
    t = threading.Thread(target=gui)
    t.start()
    main()
