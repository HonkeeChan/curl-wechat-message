
class A:
    def fun1(self):
        print 'A fun1'
    def fun2(self):
        print 'A fun2'

class B(A):
    def fun1(self):
        A.fun1(self)
        print 'B fun1'


if __name__ == '__main__':
    a = A()
    a.fun1()
    a.fun2()
    b = B()
    b.fun1()
    b.fun2()