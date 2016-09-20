# -*- coding: utf8 -*-
from Tkinter import *
import time
import threading

con = threading.Condition()
newMenu = False

def printItem():
    print 'Python = ',vPython.get() == True
    print 'PHP = ',vPHP.get() == True
    print 'CPP = ',vCPP.get() == True
    print 'C = ',vC.get() == True
    print 'Java = ',vJava.get() == True
    print 'JavaScript = ',vJavaScript.get() == True
    print 'VBScript = ',vVBScript.get() == True

def createMenu():
    print 'create new menu'
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff = 0)
    for k,v in {'的方法a':vPython,
                   '的方法b':vPHP,
                   '的方法c':vCPP,
                   '的方法d':vC}.items():
        filemenu.add_checkbutton(label = k,command = printItem,variable = v)
    menubar.add_cascade(label = 'Language',menu = filemenu)
    root['menu'] = menubar

def gui():
    global root
    root = Tk()
    global vPython 
    global vPHP     
    global vCPP    
    global vC        
    global vJava    
    global vJavaScript 
    global vVBScript  
    global newMenu
    vPython = BooleanVar()
    vVBScript = BooleanVar()
    vJavaScript = BooleanVar()
    vPHP = BooleanVar()
    vJava = BooleanVar()
    vC = BooleanVar()
    vCPP = BooleanVar()
    #每次打印出各个变量的当前值
    while True:
        if con.acquire():
            if not newMenu:
                con.wait()
            else:
                createMenu()
                print 'new menu to false'
                newMenu = False
            con.release()
    
    raw_input('hello')

t = threading.Thread(target=gui)
t.start()
while True:
    time.sleep(5)
    print 'wake up... '
    if con.acquire():
        if not newMenu:
            print 'new menu to true'
            newMenu = True
            con.notify()
        con.release()


