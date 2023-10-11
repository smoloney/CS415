#Authors: Sean Moloney and Jon Killinger
#Class : CS 415
#Assignment: Project 1

#In order to run this program, compile it wil python2 project.py

# all the computations for HW 1 shall be done using binary arithmetic
# only the user input and the final output will be in decimal.
# the two functions dec2bin and bin2dec provide I/O conversion between
# binary and decimal.

# functions provided: Add, Mult, divide and many supporting functions such as
# Compare to compare two unbounded integers, bin2dec and dec2bin etc.

# missing functions: sub which performs subtraction and Divide which is the decimal version
# of divide, and also a solution to Problem 3.

########################################################
### SAMPLE INPUT/OUTPUT                             ###
########################################################


##########################################################

import random
import sys
import time

sys.setrecursionlimit(10000000)

from random import *
password=1234
def shift(A, n):
    if n == 0:
        return A
    return [0]+shift(A, n-1)
    
def mult(X, Y):
    # mutiplies two arrays of binary numbers
    # with LSB stored in index 0
    if zero(Y):
        return [0]
    Z = mult(X, div2(Y))
    if even(Y):
        return add(Z, Z)
    else:
        return add(X, add(Z, Z))

def Mult(X, Y):
    X1 = dec2bin(X)
    Y1 = dec2bin(Y)
    return bin2dec(mult(X1,Y1))

def zero(X):
    # test if the input binary number is 0
    # we use both [] and [0, 0, ..., 0] to represent 0
    if len(X) == 0:
        return True
    else:
        for j in range(len(X)):
            if X[j] == 1:
                return False
    return True

def div2(Y):
    if len(Y) == 0:
        return Y
    else:
        return Y[1:]

def even(X):
    if ((len(X) == 0) or (X[0] == 0)):
        return True
    else:
        return False


def add(A, B):
    A1 = A[:]
    B1 = B[:]
    n = len(A1)
    m = len(B1)
    if n < m:
        for j in range(len(B1)-len(A1)):
            A1.append(0)
    else:
        for j in range(len(A1)-len(B1)):
            B1.append(0)
    N = max(m, n)
    C = []
    carry = 0
    for j in range(N):
        C.append(exc_or(A1[j], B1[j], carry))
        carry = nextcarry(carry, A1[j], B1[j])
    if carry == 1:
        C.append(carry)
    return C

def Add(A,B):
    return bin2dec(add(dec2bin(A), dec2bin(B)))

def exc_or(a, b, c):
    return (a ^ (b ^ c))

def nextcarry(a, b, c):
    if ((a & b) | (b & c) | (c & a)):
        return 1
    else:
        return 0 
        
def bin2dec(A):
    if len(A) == 0:
        return 0
    val = A[0]
    pow = 2
    for j in range(1, len(A)):
        val = val + pow * A[j]
        pow = pow * 2
    return val

def reverse(A):
    B = A[::-1]
    return B

def trim(A):
    if len(A) == 0:
        return A
    A1 = reverse(A)
    while ((not (len(A1) == 0)) and (A1[0] == 0)):
        A1.pop(0)
    return reverse(A1)


def compare(A, B):
    # compares A and B outputs 1 if A > B, 2 if B > A and 0 if A == B
    A1 = reverse(trim(A))
    A2 = reverse(trim(B))
    if len(A1) > len(A2):
        return 1
    elif len(A1) < len(A2):
        return 2
    else:
        for j in range(len(A1)):
            if A1[j] > A2[j]:
                return 1
            elif A1[j] < A2[j]:
                return 2
        return 0

def Compare(A, B):
    return bin2dec(compare(dec2bin(A), dec2bin(B)))

def dec2bin(n):
    if n == 0:
        return []
    m = n/2
    A = dec2bin(m)
    fbit = n % 2
    return [fbit] + A
    
def divide(X, Y):
    # finds quotient and remainder when A is divided by B
    if zero(X):
        return ([],[])
    (q,r) = divide(div2(X), Y)
    q = add(q, q)
    r = add(r, r)
    if (not even(X)):
        r = add(r,[1])
    if (not compare(r,Y)== 2):
        r = sub(r, Y)
        q = add(q, [1])
    return (q,r)

def map(v):
    if v==[]:
        return '0'
    elif v ==[0]:
        return '0'
    elif v == [1]:
        return '1'
    elif v == [0,1]:
        return '2'
    elif v == [1,1]:
        return '3'
    elif v == [0,0,1]:
        return '4'
    elif v == [1,0,1]:
        return '5'
    elif v == [0,1,1]:
        return '6'
    elif v == [1,1,1]:
        return '7'
    elif v == [0,0,0,1]:
        return '8'
    elif v == [1,0,0,1]:
        return '9'   
        
def bin2dec1(n):
    if len(n) <= 3:
        return map(n)
    else:
        temp1, temp2 = divide(n, [0,1,0,1])
        return bin2dec1(trim(temp1)) + map(trim(temp2))

def sub(A, B):
    A1 = A[:]
    B1 = B[:]
    n = len(A1)
    m = len(B1)
    if n < m:
        for j in range(len(B1)-len(A1)):
            A1.append(0)
    else:
        for j in range(len(A1)-len(B1)):
            B1.append(0)
            
    B1 = twoComplement(B1)
    B1 = add(B1,[1])
    N = max(m, n)
    C = []
    carry = 0
    for j in range(N):
        C.append(exc_or(A1[j], B1[j], carry))
        carry = nextcarry(carry, A1[j], B1[j])

    return C

def twoComplement(a):
    
    for i in range (len(a)):
        if a[i] & 1 == 1:
            a[i] = 0
        else:
            a[i] = 1
            
    return a

        
def problem1a(a,b,c,d):
    aRaisedb = expo(a, b)
    cRaisedd = expo(c, d)
    if compare(aRaisedb, cRaisedd) == 2:
        remainder = sub(cRaisedd, aRaisedb)
        r = "-" + str(bin2dec(remainder))
        print(r)
    else:
        remainder = sub(aRaisedb, cRaisedd)
        print(bin2dec(remainder))



def problem1b(a, b, c, d):
    aRaisedb = expo(a, b)
    cRaisedd = expo(c, d)
    
    if compare(aRaisedb, cRaisedd) == 2:
       print("Q: 1", "R: ", bin2dec(sub(cRaisedd, aRaisedb)))
       return None
    quotient, remainder = divide(aRaisedb, cRaisedd)
    print("Q:", bin2dec(quotient), "R:", bin2dec(remainder))


def fractAdd(p,q,r,s):
    num = add(mult(p,s), mult(q,r))
    den = mult(q,s)
    return (num,den)

def gcd(a, b):
    if( zero(b) or (compare(a,b)==0)):
        return a
    if(compare(a,b)==2):
        return gcd(b,a)
    else:
        quotient, remainder = divide(a,b)
        return gcd(b, remainder)
    
def problem1c(a):
    summedNum = [1]
    summedDenom = [1]

    for i in range(2,bin2dec(a)+1):
        summedNum, summedDenom = fractAdd([1],dec2bin(i),summedNum,summedDenom)

    g = gcd(summedNum,summedDenom)
    (p1, q1) = divide(summedNum, g)
    (p2, q2) = divide(summedDenom, g)
    print(bin2dec(p1),bin2dec(p2))

def expo(a, b):
    if b == dec2bin(1):
        return a
    if b == dec2bin(2):
        return mult(a, a)
    if(even(b)):
        return expo(expo(a, div2(b)), [0,1])
    else:
        return mult(a,(expo(expo(a,div2(sub(b, [1]))),dec2bin(2))))

def main():
    
    end = 1
    while(end != 0):
        num = int(input("Press 1 for subtraction. \n Press 2 for division. \n Press 3 for problem1c.\n Press 0 to quit."))
        
        if num == 1 or num == 2:
            a = dec2bin(int(input("First number: ")))
            b = dec2bin(int(input("To the power of: ")))
            c = dec2bin(int(input ("Second number: ")))
            d = dec2bin(int(input("To the power of: ")))

            if num == 1:
                problem1a(a, b, c, d)
            else:
                problem1b(a, b, c ,d)

        elif num == 3:
            a = dec2bin(int(input("Enter a number: ")))
            problem1c(a)
        else:
            sys.exit()

main()














