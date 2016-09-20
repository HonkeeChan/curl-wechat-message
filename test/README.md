#学习使用tkinter的demo

###tk_getstart.py
列出两个ListBox控件

###tk_menu_checkbtn_cond.py
因为tkinter是线程不安全的，我需要有一个线程A在循环中忙等待，另一个线程B生成Tkinter界面，并且通过A产生的数据来动态更变界面的Menu显示。 

我想到的第一个方法是：将需要显示的变量设置为全局变量，线程B生成Tkinter之后就root.mainloop()忙等，线程A数据发生变化之后，在线程A那里通过修改全局变量的方法修改Tkinter的显示，这个方法在ubuntu中可以运行，但是到了Windows下出错，错误信息大致是`_tkinter.tclerror out of stack space`,[google搜索得到的答案是Tkinter不能多线程访问](http://stackoverflow.com/questions/22541693/tkinter-and-thread-out-of-stack-space-infinite-loop)。

那么我想到另外一个方法，就是所有关于界面显示的控件都交给B线程来操作，线程A，B的共享信息作为全局变量，通过条件变量来通知。这个方法似乎行不通，创建菜单的函数有调用，可是界面就是没有显示。于是有了下面这个方法。

###tk_menu_checktn.py
Tkinter的after函数，让窗体定期调用一个指定的函数。我这里让窗体定期访问A，B线程共享的信息刷新窗体，A线程去修改那个共享的信息。