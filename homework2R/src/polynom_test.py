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
        self.n=n
        self.i=i%n #fugly but works with negative numbers which is nice (but platform dependent perhaps)

    def __str__(self):
        """
        You are on your own on tracking n, mostly one has the same n
        """
        return str(self.i)

    def __eq__(self,other):
        """
        NOOOOT!! Must be of the same Zn to be the same
        """
        if(isinstance(other,int)):
            return self.i==other
        return self.i==other.i
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
        for i,c_i in enumerate(reversed(self.c)):
            if((len(self)-i-1)>1): #fugly with double reverse TODO fix
                output+=str(c_i)
                output+="X^"+str(len(self)-i-1)+"+"
            elif((len(self)-i-1)==1):
                output+=str(c_i)+"X+"
            else:
                output+=str(c_i)
        return output

    def __eq__(self,other):
        N=len(self)
        M=len(other)
        #if all elements is equal and the part hanging outside is all zero then the polynoms are equal
        pseudoeq=all(map(lambda (a,b):a==b,zip(self.c,other.c)))
        if(N==M):#fugly code #TODO fixit 
            return pseudoeq 
        elif(M<N):
            return pseudoeq and reduce(operator.add,self.c[M:N])==0
        else:#(N<M)
            return pseudoeq and reduce(operator.add,other.c[N:M])==0

    def __neq__(self,other):
        return not operator.__eq__(self,other)

    def __add__(self,other):
        c_res=map(lambda (i,j):i+j,itt.izip_longest(self.c,other.c,fillvalue=0))
        return Polynom(c_res)
    
    def __len__(self):
        return len(self.c)

    def __mul__(self,other):
        #cauchy
        c_n=[0]*(len(self)+len(other)-1)

        for k in range(len(c_n)): #a little bit fugly with a forloop but gets nasty without
            filtered=filter(lambda (i,j):i+j==k,itt.product(range(len(self)),range(len(other))))
            c_n[k] = reduce(operator.add,map(lambda (i,j): self.c[i]*other.c[j],filtered))
        
        return Polynom(c_n)


pa=Polynom([1,2,3])
print pa
pb=Polynom([1,2,3])
print pb
print pa+pb
print pa*pb

print pa==pb
print pa+pb!=pa
print pa==Polynom([1,2,3])
print pa==Polynom([1,2,3,0])
print not pa==Polynom([1,2,3,0,1])

m=2
degree=3

Zm=map(lambda i:Zn(m,i),range(m))

PZm=map(lambda c:Polynom(c),itt.product(Zm,repeat=(degree+1)))

#for f in PZm:
#    print f

F=Polynom(map(lambda i:Zn(m,i),[1,0,-1,0,1])) #fugly since -1%m can be machinedependant

#print F 

factors=filter(lambda (f,g):f*g==F,itt.product(PZm,repeat=2))

for f,g in factors:
    print str(f)+"*"+str(g)+"="+str(f*g)

