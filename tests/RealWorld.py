from pybench import Test
import random
# this pollutes the namespace quite a bit
#from sage.all_cmdline import *

class ZBlowup(Test):
    version=1.0
    operations = 1
    rounds = 1
    def test(self):
        from sage.all_cmdline import Integer, ellipsis_range,var,uniq,\
                set_random_seed,expand
        from itertools import izip

        print "Blowup"
        for _ in xrange(self.rounds):
            def blowup(L,n):
                R=[e for e in L]
                for i in xrange(n):
                    R=[e*f for e in L for f in R]
                return R
            (x,y)=var('x,y')
            L = [x,y]
            
            L=blowup(L, 8)
            R=[]
            for (pt,e) in enumerate(L):
                for f in L[pt+1:]:
                    R.append((e-f).is_trivial_zero())
    def calibrate(self):
        from sage.all_cmdline import Integer, ellipsis_range,var,uniq,\
                set_random_seed
        set_random_seed(0)
        random.seed(0)
        print "blowup calibrate"
        for _ in xrange(self.rounds):
            def blowup(L,n):
                R=[e for e in L]
                for i in xrange(n):
                    R=[e*f for e in L for f in R] 
                return R
            (x,y)=var('x,y')
            L = [x,y]
            L=blowup(L, 8)


class RealPart(Test):
    version=1.0
    operations = 1
    rounds = 1
    def test(self):
        from sage.all_cmdline import Integer, sqrt, real, i
        for _ in xrange(self.rounds):
            _sage_const_3 = Integer(3)
            _sage_const_2 = Integer(2)
            _sage_const_1 = Integer(1)
            def f(z): 
                return sqrt(_sage_const_1 /_sage_const_3 )*z**_sage_const_2  + i/_sage_const_3 
            real(f(f(f(f(f(i/_sage_const_2 ))))))

    def calibrate(self):
        from sage.all_cmdline import Integer, sqrt, i
        for _ in xrange(self.rounds):
            _sage_const_3 = Integer(3)
            _sage_const_2 = Integer(2)
            _sage_const_1 = Integer(1)
            def f(z): 
                return sqrt(_sage_const_1 /_sage_const_3 )*z**_sage_const_2  + i/_sage_const_3 

class Hermite(Test):
    version=1.0
    operations = 1
    rounds = 1
    def test(self):
        """
        def hermite(n,y):
            if n == 1: return 2*y
            if n == 0: return 1
            return expand(2*y*hermite(n-1,y) - 2*(n-1)*hermite(n-2,y))

            time hermite(15,var('y'))
        """
        from sage.all_cmdline import Integer, sqrt, real, var, expand
        for _ in xrange(self.rounds):
            _sage_const_2 = Integer(2)
            _sage_const_1 = Integer(1)
            _sage_const_0 = Integer(0)
            _sage_const_15 = Integer(18)
            def hermite(n,y):
                if n == _sage_const_1 : return _sage_const_2 *y
                if n == _sage_const_0 : return _sage_const_1 
                return expand(_sage_const_2 *y*hermite(n-_sage_const_1 ,y) - _sage_const_2 *(n-_sage_const_1 )*hermite(n-_sage_const_2 ,y))
            hermite(_sage_const_15 ,var('y'))

    def calibrate(self):
        from sage.all_cmdline import Integer, real, expand
        for _ in xrange(self.rounds):
            _sage_const_2 = Integer(2)
            _sage_const_1 = Integer(1)
            _sage_const_0 = Integer(0)
            _sage_const_15 = Integer(15)
            def hermite(n,y):
                if n == _sage_const_1 : return _sage_const_2 *y
                if n == _sage_const_0 : return _sage_const_1 
                return expand(_sage_const_2 *y*hermite(n-_sage_const_1 ,y) - _sage_const_2 *(n-_sage_const_1 )*hermite(n-_sage_const_2 ,y))

class Equality(Test):   #a lot of overhead for this test
    version=1.0
    operations = 1
    rounds = 1
    def test(self):
        """
        sage: time v = [-pi,-pi+1/10..,pi]
        """
        from sage.all_cmdline import Integer,var
        for _ in xrange(self.rounds):
            _sage_const_10 = Integer(10)   
            l=[]
            for j in xrange(1,10):
                l.append("q"+str(j))
            s=reduce(lambda a,b: a+","+b,l)
            sp=reduce(lambda a,b: a+"+"+b,l)
            var(s) 
            f = eval(sp)
            a = [bool(f==f) for _ in range(_sage_const_10 )]
    def calibrate(self):
        from sage.all_cmdline import Integer,var
        for _ in xrange(self.rounds):
            _sage_const_10 = Integer(10)    
            l=[]
            for j in xrange(1,10):
                l.append("q"+str(j))
            s=reduce(lambda a,b: a+","+b,l)
            sp=reduce(lambda a,b: a+"+"+b,l)
            var(s) 
            f = eval(sp)


class Cardinality(Test):
    version=1.0
    operations = 1
    rounds = 250
    def test(self):
        """
        u = [e, pi, sqrt(2)]
        time Tuples(u,3).cardinality()
        """
        from sage.all_cmdline import Integer, sqrt, e, pi, Tuples 
        for _ in xrange(self.rounds):
            _sage_const_3 = Integer(3); 
            _sage_const_2 = Integer(2)
            u = [e, pi, sqrt(_sage_const_2 )]
            Tuples(u,_sage_const_3 ).cardinality()
    def calibrate(self):
        from sage.all_cmdline import Integer, sqrt, e, pi, Tuples 
        for _ in xrange(self.rounds):
            _sage_const_3 = Integer(3); 
            _sage_const_2 = Integer(2)
            u = [e, pi, sqrt(_sage_const_2 )]



class Simplify(Test):
    version=1.0
    operations = 1
    rounds = 1
    def test(self):
        from sage.all_cmdline import Integer, sin 
        for _ in xrange(self.rounds):
            _sage_const_100 = Integer(400)
            sum(((x+sin(i))/x+(x-sin(i))/x) for i in xrange(_sage_const_100 )) 

    def calibrate(self):
        from sage.all_cmdline import Integer
        for _ in xrange(self.rounds):
            _sage_const_100 = Integer(400)

class Evaluate(Test):
    version=1.0
    operations = 1
    rounds = 1
    def test(self):
        from sage.all_cmdline import Integer, random,var 
        for _ in xrange(self.rounds):
            _sage_const_3 = Integer(3)
            _sage_const_32 = Integer(32)
            _sage_const_45 = Integer(45)
            _sage_const_4 = Integer(4)
            _sage_const_9 = Integer(9)
            _sage_const_12 = Integer(12)
            _sage_const_10 = Integer(9)
            _sage_const_18 = Integer(18)
            _sage_const_21 = Integer(21)
            _sage_const_34 = Integer(34)
            _sage_const_24 = Integer(24)
            x=var('x') 
            f = x**_sage_const_24 +_sage_const_34 *x**_sage_const_12 +_sage_const_45 *x**_sage_const_3 +_sage_const_9 *x**_sage_const_18  +_sage_const_34 *x**_sage_const_10 + _sage_const_32 *x**_sage_const_21 
            a = [f(x=random()) for _ in xrange(_sage_const_10 **_sage_const_4 )] 

    def calibrate(self):
        from sage.all_cmdline import Integer,var
        for _ in xrange(self.rounds):
            _sage_const_3 = Integer(3)
            _sage_const_32 = Integer(32)
            _sage_const_45 = Integer(45)
            _sage_const_4 = Integer(4)
            _sage_const_9 = Integer(9)
            _sage_const_12 = Integer(12)
            _sage_const_10 = Integer(10)
            _sage_const_18 = Integer(18)
            _sage_const_21 = Integer(21)
            _sage_const_34 = Integer(34)
            _sage_const_24 = Integer(24)
            x=var('x') 
            f = x**_sage_const_24 +_sage_const_34 *x**_sage_const_12 +_sage_const_45 *x**_sage_const_3 +_sage_const_9 *x**_sage_const_18  +_sage_const_34 *x**_sage_const_10 + _sage_const_32 *x**_sage_const_21 
class Riemann(Test):
    version=1.0
    operations = 1
    rounds = 1
    def test(self):
        from sage.all_cmdline import Integer, var 
        for _ in xrange(self.rounds):
            _sage_const_2 = Integer(2)
            _sage_const_10 = Integer(11)
            _sage_const_0 = Integer(0)
            _sage_const_5 = Integer(5)
            _sage_const_4 = Integer(4)
            def right(f,a,b,n):
                Deltax = (b-a)/n; c=a; est=_sage_const_0 
                for _ in range(n):
                    c += Deltax
                    est += f(x=c)
                return est*Deltax
            x=var('x')
            v=right(f=x**_sage_const_2 ,a=_sage_const_0 ,b=_sage_const_5 ,n=_sage_const_10 **_sage_const_4 ); 
    def calibrate(self):
        from sage.all_cmdline import Integer,var
        for _ in xrange(self.rounds):
            _sage_const_2 = Integer(2); _sage_const_10 = Integer(10); _sage_const_0 = Integer(0); _sage_const_5 = Integer(5); _sage_const_4 = Integer(4)
            def right(f,a,b,n):
                Deltax = (b-a)/n; c=a; est=_sage_const_0 
                for _ in range(n):
                    c += Deltax
                    est += f(x=c)
                return est*Deltax
            x=var('x')
"""
class Factor(Test):
    version=1.0
    operations = 1
    rounds = 1
    def test(self):
        from sage.all_cmdline import Integer, factor,var,pi 
        for _ in xrange(self.rounds):
            _sage_const_20 = Integer(20); _sage_const_5 = Integer(5)
            var('x,y')
            factor(x**_sage_const_20  - pi**_sage_const_5 *y**_sage_const_20 ); 
    def calibrate(self):
        from sage.all_cmdline import Integer,var
        for _ in xrange(self.rounds):
            _sage_const_20 = Integer(20); _sage_const_5 = Integer(5)
            var('x,y')
"""

class EquallySpacedList(Test):
    version=1.0
    operations = 1
    rounds = 1
    def test(self):
        from sage.all_cmdline import Integer, ellipsis_range, pi 
        for _ in xrange(self.rounds):
            _sage_const_1 = Integer(1)
            _sage_const_10 = Integer(40000)
            v = (ellipsis_range(-pi,-pi+_sage_const_1 /_sage_const_10 ,Ellipsis,pi))
    def calibrate(self):
        from sage.all_cmdline import Integer
        for _ in xrange(self.rounds):
            _sage_const_1 = Integer(1)
            _sage_const_10 = Integer(1000)

class ComplexList(Test):
    version=1.0
    operations = 1
    rounds = 1 
    def test(self):
        from sage.all_cmdline import Integer, random, ellipsis_range,I
        for _ in xrange(self.rounds):
            _sage_const_0 = Integer(0)
            _sage_const_1000 = Integer(2000)
            a = [random() + random()*I for w in (ellipsis_range(_sage_const_0 ,Ellipsis,_sage_const_1000 ))]
    def calibrate(self):
        from sage.all_cmdline import Integer
        for _ in xrange(self.rounds):
            _sage_const_0 = Integer(0)
            _sage_const_1000 = Integer(2000)

