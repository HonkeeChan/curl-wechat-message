#encoding: utf8

import threading
import time 

def fun_throw_excepthon():
    global exception_var
    exception_var = 10
    cnt = 0 
    for i in range(100):
        time.sleep(2)
        print 'normal var', normal_var
        cnt = cnt + 1
        print 'cnt', cnt
        if cnt > 5:
            cnt / 0
        

def normalfun():
    global normal_var
    normal_var  = 10
    cnt = 0 
    for i in range(100):
        time.sleep(2)
        print 'exception var', exception_var
        cnt = cnt + 1
        print 'cnt', cnt

        

if __name__ == '__main__':
    # t = threading.Thread(target = normalfun)
    # t.start()
    # fun_throw_excepthon()
    t = threading.Thread(target = fun_throw_excepthon)
    t.start()
    normalfun()