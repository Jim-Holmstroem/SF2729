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
m=18
Z=map(lambda i:Zn(N,i),range(N)) #Generate all elements
Zero=Zn(N,0) #Generate zero
One=Zn(N,1) #Generate one

#========Assignment=============================
UZ=filter(lambda b:any(map(lambda g:g*b==b*g==One,Z)),Z) #\exists g:gb=bg=1

print "g^18=1 forall g?",all(map(lambda g:g**18==One,UZ)) #is all g^18= \forall g \in U(Z)
 
