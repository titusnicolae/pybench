from pybench import Test

# this pollutes the namespace quite a bit
#from sage.all_cmdline import *
 
class S1(Test):
    version=2.0
    operations = 1
    rounds = 1
    def test(self):
        from sage.all_cmdline import Integer, sqrt, real
        for i in xrange(self.rounds):
            _sage_const_1 = Integer(1)
            _sage_const_7 = Integer(7)
            var('x,y,z')
            f = (x+y+z+_sage_const_1 )**_sage_const_7 
            g = expand(f*(f+_sage_const_1 )); 
    def calibrate(self):
        for i in xrange(self.rounds):
            _sage_const_1 = Integer(1)
            _sage_const_7 = Integer(7)
            var('x,y,z')
            f = (x+y+z+_sage_const_1 )**_sage_const_7 

class S2(Test):
    version=2.0
    operations = 1
    rounds = 1
    def test(self):
        from sage.all_cmdline import Integer, sqrt, real
        for i in xrange(self.rounds):
            _sage_const_100 = Integer(100)
            x,y,z=var('x,y,z')
            a = expand((x**sin(x) + y**cos(y) - z**(x+y))**_sage_const_100 ); 
    def calibrate(self):
        for i in xrange(self.rounds):
            _sage_const_100 = Integer(100)
            x,y,z=var('x,y,z')

class S3(Test):
    version=2.0
    operations = 1
    rounds = 1
    def test(self):
        from sage.all_cmdline import Integer, sqrt, real
        for i in xrange(self.rounds):
            _sage_const_50 = Integer(50)
            x=var('x')
            y=var('y')
            z=var('z')
            f=expand((x**y+y**z+z**x)**_sage_const_50 )
    def calibrate(self):
        for i in xrange(self.rounds):
            _sage_const_50 = Integer(50)
            x=var('x')
            y=var('y')
            z=var('z')

class S4(Test):
    version=2.0
    operations = 1
    rounds = 1
    def test(self):
        from sage.all_cmdline import Integer, sqrt, real, taylor
        for i in xrange(self.rounds):
            _sage_const_0 = Integer(0)
            _sage_const_1000 = Integer(1000)
            x=var('x')
            w = (sin(x)*cos(x)).taylor(x,_sage_const_0 ,_sage_const_1000 ) 
     def calibrate(self):
        for i in xrange(self.rounds):
            _sage_const_0 = Integer(0)
            _sage_const_1000 = Integer(1000)
            x=var('x')
