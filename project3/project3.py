"""
Authors: Sean Moloney and Jon Killinger
Class: CS 415
Assignment: Project 3
Description: This project implents FFT, IFFT and component multiplication.
Executes by running: python2 project3.py
"""

import random
import cmath
import math
import sys
import timeit
import time


#sys.setrecursionlimit(10000000)

def appendZeros(array2append, n):
    """
    Input: Array, number of 0s to append
    Output: Array
    Description: This function takes in an array and appends n number of 0s to the array.
    """
    for i in range(0, n):
        array2append.append(0)
    return array2append

def genPoly(n):
    """
    Input: An integer
    Output: Integer array
    Description: This function takes in an integer, n, and will generate a random polynomial of
    n degrees.  It will do so by generating an array and appending 1 or 0 to each element of the array which
    will stand for the coeffiecent for each degree.
    """
    v = []
    for i in range(0, n + 1):
        v.append(random.uniform(0,1))
    v = appendZeros(v,n + 1)
    return v

def splitArray(array2split):
    """
    Input: An array
    Output: 2 arrays, each half the size of the original array.
    Description: This function will take in an array and split this original array
    into two different arrays.  One array will contain all data from the odd indexes.  The other
    will contain the data from the even indexes. 
    """
    oddArray = []
    evenArray = []
    for i in range(len(array2split)):
        if(i % 2 == 0):
            evenArray.append(array2split[i])
        else:
            oddArray.append(array2split[i])
    return (evenArray, oddArray)

def FFT(inputArray,w):
    """
    Input: Array, integer
    Output: Array with Fast Fourier Transformed performed on it.
    Desciption: This function will take in an array and the nth root of unity.  It will then perform the FFT algorithm on the array.
    """

    if len(inputArray) == 1:
        return inputArray

    evenArray, oddArray = splitArray(inputArray)
    s = FFT(evenArray,w*w)
    sPrime = FFT(oddArray,w*w)

    r = appendZeros([],len(inputArray))

    for j in range(0,len(inputArray)/2 ):
        r[j] = s[j] + ( pow(w,j) * sPrime[j] )
        r[j + len(inputArray) / 2] = s[j] - ( pow(w,j) * sPrime[j])
    return r

def compMult(u,v):
    """
    Input: 2 arrays
    Output: One array
    Description:  This function will perform component multiplcation on the two arrays by multipying each element
    of u and v together and placing it into a third array.
    """
    result = []
    for i in range(0,len(u)):
        result.append(u[i] * v[i])
    return result

def IFFT(inputArray,myW):
    """
    Input: An array and the nth root of unity
    Output: Inverse Fast Fourier Transform of the array
    Description:  This function takes in an array and the nth root of unity.  It will first perform FFT on the array.  
    Next, the function will create a new array and the first value from the FFT array will be appended to it. Then, we will reverse
    all of the FFT array and divide each element by the length of the FFT array.
    """
    inputArray = FFT(inputArray,myW)
    n = len(inputArray)
    new = []
    new.append(inputArray[0])

    i = n - 1
    while i != 0:
        new.append(inputArray[i])
        i = i - 1

    new = [round((x  * 1/float(n)).real,2) for x in new]

    return new

def slowPolyMult(a,b):
    """
    Input: 2 integer arrays
    Output: Product of the two arrays
    Description: This function will take in two integer arrays.  It will then loop through each element of the first array and multiply it by
    by the second array at k - j. It will add this to the previous sum and append it to a new array.

    """
    result = []
    result = appendZeros(result,len(a))

    kLim = len(a)
    
    for k in range(0,kLim):
        mySum = 0
        j = 0
        while j <= k:
            myProduct = a[j] * b[k-j]
            mySum = mySum + myProduct
            j = j + 1
        result[k] = round(mySum,2)
    return result

def main():
    degree = input('Enter degree: ')
    v = genPoly(degree)
    u = genPoly(degree)

    myW = cmath.exp((2*cmath.pi*1j)/len(v))

    start_time = time.time()  
    FFTV = FFT(v,myW)
    FFTU = FFT(u,myW)
    componentMult = compMult(FFTV,FFTU)
    myIFFT = IFFT(componentMult,myW)
    print("FFT CPU time: ( %s seconds )" % (time.time() - start_time))  

    start_time = time.time()  
    mySlowConvolution = slowPolyMult(u,v)
    print("Slow Poly Multiply CPU time: ( %s seconds )" % (time.time() - start_time))  

    if(degree <= 100):
        print("v: ",v)
        print("u: ",u)
        print("Result of homegrown inverse DFT convolution",myIFFT)
        print("Result of homegrown n-squared complexity convolution", mySlowConvolution)

    else:

        f = open('out.txt', 'w')
    
        #TODO: NEWLINES
        print >> f, 'Input degree n:', degree
        print >> f, ' Generated polynomial u:', u
        print >> f, ' Generated polynomial v:', v
        print >> f, ' My FFT convolve:', myIFFT
        print >> f, ' My slow convolve:', mySlowConvolution
        
    

main()




    


