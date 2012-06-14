from pybench import Test

# this pollutes the namespace quite a bit
#from sage.all_cmdline import *
 
class ExpandTrinomial(Test):
    version=1.0
    operations = 1
    rounds = 1
    def test(self):
        from sage.all_cmdline import Integer, expand, var
        for i in xrange(self.rounds):
            _sage_const_1 = Integer(1)
            _sage_const_7 = Integer(10)
            var('x,y,z')
            f = (x+y+z+_sage_const_1 )**_sage_const_7 
            g = expand(f*(f+_sage_const_1 )); 
    def calibrate(self):
        from sage.all_cmdline import Integer, var
        for i in xrange(self.rounds):
            _sage_const_1 = Integer(1)
            _sage_const_7 = Integer(10)
            var('x,y,z')
            f = (x+y+z+_sage_const_1 )**_sage_const_7 


class ExpandTrig(Test):
    version=1.0
    operations = 1
    rounds = 1
    def test(self):
        from sage.all_cmdline import Integer, expand, sin, cos, var
        for i in xrange(self.rounds):
            _sage_const_100 = Integer(200)
            x,y,z=var('x,y,z')
            a = expand((x**sin(x) + y**cos(y) - z**(x+y))**_sage_const_100 ); 
    def calibrate(self):
        from sage.all_cmdline import Integer, var 
        for i in xrange(self.rounds):
            _sage_const_100 = Integer(120)
            x,y,z=var('x,y,z')


class DiffExpansion(Test):
    version=1.0
    operations = 1
    rounds = 1
    def test(self):
        from sage.all_cmdline import Integer, expand, var, diff 
        for i in xrange(self.rounds):
            _sage_const_50 = Integer(110)
            x=var('x')
            y=var('y')
            z=var('z')
            f=expand((x**y+y**z+z**x)**_sage_const_50)
            g = f.diff(x)
    def calibrate(self):
        from sage.all_cmdline import Integer, var, expand
        for i in xrange(self.rounds):
            _sage_const_50 = Integer(55)
            x=var('x')
            y=var('y')
            z=var('z')
            f=expand((x**y+y**z+z**x)**_sage_const_50)


class Taylor(Test):
    version=1.0
    operations = 1
    rounds = 1
    def test(self):
        from sage.all_cmdline import Integer, var, sin, cos, taylor
        for i in xrange(self.rounds):
            _sage_const_0 = Integer(0)
            _sage_const_1000 = Integer(350)
            x=var('x')
            w = (sin(x)*cos(x)).taylor(x,_sage_const_0 ,_sage_const_1000 ) 
    def calibrate(self):
        from sage.all_cmdline import Integer, var 
        for i in xrange(self.rounds):
            _sage_const_0 = Integer(0)
            _sage_const_1000 = Integer(200)
            x=var('x')

