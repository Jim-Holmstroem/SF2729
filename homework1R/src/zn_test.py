import operator
import copy
import itertools as itt
import string
import math

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
    def __rmul__(self,other): #Commutative
        return operator.__mul__(self,other)
    def __pow__(self,m):
        """
        return g**n
        """
        return Zn(self.n,(self.i**m)%self.n)
    
    def __hash__(self):
        return self.i

def print_listing(listing):
    line=""
    for g,has in listing.iteritems():
        line+=(str(g)+" | ")
        for h in has:
            line+=string.center(str(h),6)
        print line
        line=""

N=1026

divisors=filter(lambda a:operator.mod(N,a)==0,range(1,int(math.sqrt(N))))

Z=map(lambda i:Zn(N,i),range(N))
Zero=Zn(N,0)
One=Zn(N,1)

#complete list with information
UZlist=(map(lambda g:(g,filter(lambda b:g*b==One,Z)),Z))

#pickout the elements forming U(Z)
UZ=map(lambda u:u[0],filter(lambda (key,v):len(v)!=0,UZlist)) #pickout the key

#gpows=map(lambda m:(m,map(lambda g:g**m,UZ)),divisors)
gpows=map(lambda m:(m,map(lambda g:g**m,UZ)),range(1,N))

print_listing(dict(gpows))
#print_listing(dict(UZlist))


