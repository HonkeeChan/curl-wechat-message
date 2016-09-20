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
            # print '*********************'
            # print self.group_list
            groupUsername = msg['user']['id']
            if(usernameMap.has_key(groupUsername)):
                if(usernameMap[groupUsername][1].get() == True):
                    print usernameMap[groupUsername][0], msg['content']['data']

            # print 'msg[to_user_id]', msg['to_user_id']
            # for group in self.group_list:
            #     print group
            #     if group['UserName'] == msg['user']['id']:
            #         print 'nickname,', group['NickName']
            # print msg['content']['data']
        

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
        print 'create new menu'
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
