import operator
import copy
import itertools as itt
import string
import math

#=======Printers===========================
def print_listing(listing):
    line=""
    for g,has in listing.iteritems():
        line+=(str(g)+" | ")
        for h in has:
            line+=string.center(str(h),6)
        print line
        line=""

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

#========Setup===================================
N=1026
Z=map(lambda i:Zn(N,i),range(N)) #Generate all elements
Zero=Zn(N,0) #Generate zero
One=Zn(N,1) #Generate one

#========Assignment=============================
UZinfo=(map(lambda g:(g,filter(lambda b:g*b==One,Z)),Z))

#pickout the elements forming U(Z)
UZ=map(lambda u:u[0],filter(lambda (key,v):len(v)!=0,UZinfo)) #pickout the key
print UZ

gpows=map(lambda m:(m,map(lambda g:g**m,UZ)),range(1,N))

print_listing(dict(gpows[18]))
    
