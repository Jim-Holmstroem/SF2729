import operator
import copy
import itertools as itt


def int2bits(i,n,zero_element=0,one_element=1):
    return list((zero_element,one_element)[i>>j & 1] for j in xrange(n-1,-1,-1))

def maplist(a,indices):
    return map(lambda i:operator.getitem(a,i),indices)

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
        return all(map(operator.eq,self.bits,b.bits)) #make to list, if all elements are equal
    def __ne__(self,b):
        return not operator.__eq__(self,b)

    def __add__(self,other):
        return M2R2(map(operator.xor,self.bits,b.bits))
    
    def __mul__(self,other):
        a=map(operator.and_,maplist(self.bits,[0,0,2,2]),maplist(other.bits,[0,1,0,1]))
        b=map(operator.and_,maplist(self.bits,[1,1,3,3]),maplist(other.bits,[2,3,2,3]))
        return M2R2(map(operator.xor,a,b))

def M2R2_printer(r):
    print r
    print 
    return r


def M2R2_list_printer(rs,pre_r=None):
    """
    Fundamental flaw: doesnt wrap
    pre_s is if you want to have an start M2R2 seperated from the others being first
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

Zero=M2R2(0)

R = map(lambda r:M2R2(r),range(16))
Rstar=copy.copy(R)
Rstar.remove(Zero)


mul_table=map(lambda a:map(lambda b:(0,1)[a*b==Zero],Rstar),Rstar)

dozsmatrix=map(lambda a:[a,filter(lambda b:a*b==Zero,R)],R)

for doz in dozsmatrix:
    M2R2_list_printer(doz[1],doz[0])
    print "------------------"

num_divofzero=map(sum,mul_table)
Rstar_num=zip(Rstar,num_divofzero)

Rdivofzero=map(lambda r:r[0],filter(lambda r_num:bool(r_num[1]),Rstar_num))

#M2R2_list_printer(Rdivofzero)


#Commutative? NO
#print all(map(lambda (a,b):a*b==b*a,itt.product(R,repeat=2)))



"""
Tests
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


