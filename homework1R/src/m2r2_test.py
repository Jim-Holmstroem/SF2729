import operator
import copy
import itertools as itt
import math

def int2bits(i,n,zero_element=0,one_element=1):
    return list((zero_element,one_element)[i>>j & 1] for j in xrange(n-1,-1,-1))

def maplist(a,indices):
    return map(lambda i:operator.getitem(a,i),indices)


class perm_n:
    """
    NOTE 1-indexed
    """
    perm=[] # NOTE non cyclic representation
    def __init__(self,n,elem=1):
        self.n=n
        if isinstance(elem,list):
            self.perm=elem
        else:
            assert(1<=elem<=math.factorial(n))
            self.perm=list(itt.permutations(range(1,n+1)))[elem-1]

    def __call__(self,i):
        assert(0<i<=self.n)
        return self.perm[i-1] 

    def __str__(self):
        return str(self.perm)

    def __mul__(self,other):
        assert(self.n==other.n)
        return perm_n(self.n,map(self,other.perm))

    def __eq__(self,other):
        assert(self.n==other.n)
        return all(map(operator.eq,self.perm,other.perm))

    def __ne__(self,other):
        return not operator.__eq__(self,b)

    def __hash__(self):
        return sum(map(lambda (a,k):a**k,zip(self.perm,range(1,len(self.perm)+1))))


class M2R2:
    def __init__(self,elem=0):
        """
        0->0 (important)
        one to one map (important)
        """
        if isinstance(elem,list):
            self.bits=elem
        else:
            self.bits=int2bits(elem,4)

    def __str__(self):
        return str(self.bits[0])+str(self.bits[1])+"\n"+str(self.bits[2])+str(self.bits[3]); 

    def __eq__(self,b):
        return all(map(operator.eq,self.bits,b.bits))
    def __ne__(self,b):
        return not operator.__eq__(self,b)

    def __add__(self,other):
        return M2R2(map(operator.xor,self.bits,b.bits))
    
    def __mul__(self,other):
        a=map(operator.and_,maplist(self.bits,[0,0,2,2]),maplist(other.bits,[0,1,0,1]))
        b=map(operator.and_,maplist(self.bits,[1,1,3,3]),maplist(other.bits,[2,3,2,3]))
        return M2R2(map(operator.xor,a,b))

    def __hash__(self):
        return sum(map(lambda (a,k):([2,3][a])**k,zip(self.bits,range(1,len(self.bits)+1))))

def M2R2_printer(r):
    print r
    print 
    return r

def M2R2_list_printer(rs,pre_r=None):
    """
    Fundamental flaw: doesnt wrap well
    pre_r is if you want to have an start M2R2 seperated from the others being first
    """
    firstline=""
    secondline=""
    if pre_r:
        firstline+=(str(pre_r.bits[0])+str(pre_r.bits[1]))
        firstline+=" | "
        secondline+=(str(pre_r.bits[2])+str(pre_r.bits[3]))
        secondline+=" | "

    for r in rs:
        firstline+=(str(r.bits[0])+str(r.bits[1])+ " ")
    for r in rs:
        secondline+=(str(r.bits[2])+str(r.bits[3])+" ")

    print firstline
    print secondline

#map(lambda r:M2R2_printer(M2R2(r)),range(16))


R = map(lambda r:M2R2(r),range(16)) #enumerate all elements in M_2(Z_2)
Zero=M2R2(0)
Rstar=copy.copy(R)
Rstar.remove(Zero) #R\{0}

print "Commutative?",all(map(lambda (a,b):a*b==b*a,itt.product(R,repeat=2)))

print "e="
e=filter(lambda i: all(map(lambda b:i*b==b,R)),R) #e*b=b \forall b \in R
assert len(e)==1 #generalized to ensure the uniqueness of e
e=e[0]
print e

#mul_table=map(lambda a:map(lambda b:(0,1)[a*b==Zero],Rstar),Rstar)

#dozsmatrix=map(lambda a:[a,filter(lambda b:a*b==Zero,Rstar)],Rstar) #to..TODO

#print "div of zeros"
#for doz in dozsmatrix:
#    M2R2_list_printer(doz[1],doz[0])
#    print "------------------"

#num_divofzero=map(sum,mul_table)
#Rstar_num=zip(Rstar,num_divofzero)

#Rdivofzero=map(lambda r:r[0],filter(lambda r_num:bool(r_num[1]),Rstar_num))

#TODO generalize and push to github
print "Divisors of zero"
DOZ_left=filter(lambda a:any(map(lambda b:a*b==Zero,Rstar)),Rstar) # \exists b\neq 0 :ab=0
DOZ_right=filter(lambda a:any(map(lambda b:b*a==Zero,Rstar)),Rstar)# \exists b\neq 0 :ba=0 

DOZ=filter(lambda a:a in DOZ_left,DOZ_right) #pickout the elements from left that exists in right
M2R2_list_printer(DOZ)

#M2R2_list_printer(Rdivofzero)

#M2R2_list_printer(filter(lambda i: all(map(lambda b:i*b==b,Rstar)),Rstar))


print "Group of units"
#groupofunit=map(lambda a:[a,filter(lambda b:a*b==e,Rstar)],Rstar)

UM2R2=filter(lambda a:any(map(lambda b:a*b==b*a==e,Rstar)),Rstar)
M2R2_list_printer(UM2R2)

#for unit in groupofunit:
#    M2R2_list_printer(unit[1],unit[0])
#    print "------------------"



N=3
Perms=map(lambda i:perm_n(N,i+1),range(math.factorial(N)))

#Tests with N=3, eazy to check
for x in Perms:
    print x,"(1)=" ,x(1)
    print x,"(2)=" ,x(2)
    print x,"(3)=" ,x(3)

for x,y in itt.product(Perms,repeat=2):
    print x,y,'=',x*y

def print_iso(iso):
    for x,y in iso.iteritems():
        print str(x),"=",str(y)
    print "-------------"

isos= map(lambda S:dict(zip(UM2R2,S)),itt.permutations(Perms,math.factorial(N)))

#check iso-prop for all compinations
valid_isos = filter(lambda iso: all( map(lambda (x,y):iso[x*y]==iso[x]*iso[y],itt.product(UM2R2,repeat=2)) ),isos)

print "Valid isos"
map(print_iso,valid_isos)


"""
A=M2R2([0,1,1,0])
B=M2R2([1,0,1,1])
C=M2R2([1,1,0,1])
D=M2R2([0,1,1,1])
E=M2R2([1,1,1,0])
order2=[A,B,C]
order3=[D,E]

print "E[A,B,C]"
map(lambda u:M2R2_printer(E*u),order2)

print "D[A,B,C]"
map(lambda u:M2R2_printer(D*u),order2)
"""
#print "R"
#map(lambda r:M2R2_printer(r),R)
#print "Rstar"
#map(lambda r:M2R2_printer(r),Rstar)

#print all(map(lambda r:r==r,R))
#print R[5]!=R[3]
#print R[0]!=R[12]
#print R[3]!=R[11]
#print R[2]*R[0]==Zero


