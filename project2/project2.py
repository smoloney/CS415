
from project import *
from random import *

def primality3(n, k):
    a = True
    b = True
    c = True
    d = True
    if(n >= 2):
        a = div_check(n, 2)
    if n >= 3:
        b = div_check(n, 3)
    if n >= 5:
        c = div_check(n, 5)
    if n >= 7:
        d = div_check(n, 7)
    if a == False or b == False or c == False or d == False:
            return False
            
    return primality2(n, k)



def primality2(n, k):
    a = True
    while(k > 0):
        randInt = randint(2, n-1)
        (q, r) = primality(dec2bin(randInt), dec2bin(n))
        if( r != [1]):
            a = False
        k -=1
    return a
    '''
    if(k == 0):
        return True
    randInt = randint(2, n-1)
    (q, r) = primality(dec2bin(randInt), dec2bin(n))
    print ("Returned from primality")
    print(q, r)
    if(r != [1]):
        return False
    return primality2(n, k-1)
    '''
def primality(randInt, n):
    
    return Mod_Exp_Log(randInt,sub(n, [1]), n)
    
def div_check(n, a):
    #print(" Entered div check")
    (q, r) = divide(dec2bin(n), dec2bin(a))
    if zero(r):
     #   print ("R != 0 in div check")
        return False
    else:
      #  print("Passed div_check")
        return True

    

def Mod_Exp_Log(Base, Exp, Mod):
    B = Base
    E = Exp
    M = Mod
    
    #Mod
    if (zero(M)):
        return bin2dec(expo(B, E))
    if zero(sub(M, [1])):
        return [0]

    #Exponent
    if zero(E):
        return ([1], [0])
    if(compare(E, [1])) == 0:
        (a, b) = divide(B, M)
        return (a, b)

    #Base
    
    if zero(B):
        return [0]
    if zero(sub(B, [1])):
        return [1]
    # Math time
    #Is even?
    
    if even(E):
        (val1, val2) = Mod_Exp_Log(B, divide(E, [0,1]), M)    # Need to clean this up later
        (q,r1) = divide(val1, M)
        r1 = mult(r1, r1)
        (q, r2) = divide (r1, M)
        return (val1, r2)
    else:
        
        (val1, val2) = Mod_Exp_Log(B, divide(E, [0,1]), M)   # All of this as well
        (q, r1) = divide(val1, M)
        r1 = mult(r1, r1)
        (q, base2) = divide(B, M)
        r2 = mult(r1, base2)
            
        return divide(r2, M)

def main2():
    a = primality3(53, 2)
    if(a == False):
        print("Not a prime number.")
    else:
        print("Prime Number.")

main2()
