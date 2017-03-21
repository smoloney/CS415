import numpy as np
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
    print ("Return primality 2")
    a = True
    while(k > 0):
        randInt = randint(2, n-1)
       # print("Randint", randInt)
        #print ("leaving primality2")
        r = primality(dec2bin(randInt), dec2bin(n))
        #print('R', bin2dec(r))
        
        #print(q, r)
        if( bin2dec(r) != 1):
            a = False
        k -=1
    return a

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

    
def Mod_Exp_Log(x, e, m):
    X = x
    E = e
    Y = [1]
    while not zero(E):
       # print("e",bin2dec(E))
        (p, q) = divide(E,[0,1])
        if zero(q):
            val = mult(X, X)
            (p, q) = divide(val, m)
            X = q
            (p, q) = divide(E,[0,1])
            E = p
           # print('Y', bin2dec(Y))
        else:
            val = mult(X, Y)
            (p, q) = divide(val, m)
            Y = q
            E = sub(E, [1])
            #print('Y', bin2dec(Y))
    return Y
def problem2(n, k):
    isPrime = False
    myVector = [1]
    for i in range (1, n-2):
        myVector.append(randint(0,1))
    myVector.append(1)
    isPrime = primality3(bin2dec(myVector), k)
    randInt = randint(1, n-1)
    while not isPrime:
        randInt = randint(1, n-2)
        if(myVector[randInt] == 1):
            myVector[randInt] = 0
        else:
            myVector[randInt] = 1
        isPrime = primality3(bin2dec(myVector), k)
    return myVector

def problem3(n, k):
    p = dec2bin(11)#problem2(n, k)
    q = dec2bin(7) #problem2(n, k)
    N = mult(p, q)
    E = problem2(n, k)
    
    pq = mult(sub(p, [1]), sub(q, [1]))
    i = gcd (E, pq)
    while not bin2dec(i) == 1:
        print("gcd: ", bin2dec(i))
        E = problem2(n, k)
        i = gcd(E, pq)
    print ('E', bin2dec(E))
    print('pq', bin2dec(pq))
    a, b, D = egcd(E, pq)
    print("a: ", bin2dec(a), "b: ", bin2dec(b), "D: ", bin2dec(D) )
    print( bin2dec(N), bin2dec(E), bin2dec(D))
    return (N, E, D)

def egcd(a, b):
    if zero(a):
        return (b, [0], [1])
    else:
        p, q = divide(b, a)
        g, x, y = egcd(q, a)
        m, r = divide(b, a)
        k = mult(m, x)
        l = sub(y, k)
        return g, l, x
        
              
    
def main2():
    # a,b, D = egcd(dec2bin(15), dec2bin(7))
    #print(bin2dec(a), bin2dec(b), bin2dec(D))
    # print (bin2dec(a))
    a = primality3(2,1)
    if(a == False):
        print("Not a prime number.")
    else:
        print("Prime Number.")
        print(bin2dec(problem2(50, 2)))

    (N, E, D) = problem3(10, 2)


main2()
