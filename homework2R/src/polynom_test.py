import operator
import copy
import itertools as itt
import string
import math


#=======Ring definition===================
class Zn:
    def __init__(self,n,i):
        """
        Initz Z_n with the element i
        """
        assert 0<=i<n
        self.n=n
        self.i=i

    def __str__(self):
        """
        You are on your own on tracking n, mostly one has the same n
        """
        return str(self.i)

    def __eq__(self,other):
        """
        Must be of the same Zn to be the same
        """
        return self.n==other.n and self.i==other.i
    def __ne__(self,other):
        return not operator.__eq__(self,other)
    
    def __add__(self,other):
        assert self.n==other.n
        return Zn(self.n,(self.i+other.i)%self.n)
    def __mul__(self,other):
        assert self.n==other.n #not defined else
        return Zn(self.n,(self.i*other.i)%self.n)
    def __pow__(self,m):
        """
        return g**n
        """
        return Zn(self.n,(self.i**m)%self.n)
    
    def __hash__(self):
        return self.i


class Polynom:

    
    def __init__(self,c):
        """
        Starts with the constant c_0
        """
        self.c=c

    def __str__(self):
        output=""
        for i,c_i in reversed(enumerate(self.c)):
            if(i!=0):
                output+=str(c_i)+"X^"+str(i)+"+"
            else:
                output+=str(c_i)
        return output

    def __eq__(self,other):
        return self.c==other.c
    def __neq__(self,other):
        return not operator.__eq__(self,other)

    def __add__(self,other):
        c_res=map(operator.add,itt.izip_longest(self.c,other.c,fillvalue=0))
        return Polynom(c_res)

    
    def __len__(self):
        return len(self.c)

    def __mul__(self,other):
        #cauchy
        c_n=[0]*(len(self)+len(other))

        for k in range(c_n):
            c_n[k] = map(lambda: self.c(i)*other.c(j),filter(lambda i,j:i+j==k,itt.product(range(len(self)),range(len(other)))))

        #reduce(lambda i,j:(i+j,self.c(i)+other.c(j)),
        #    
        #range(len(self)+len(other))
         


pa=Polynom([2,5,1])
print pa
pb=Polynom([1,1,2])
print pb
print pa+pb
print pa*pb



