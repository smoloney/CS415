""""
Author: Sean Moloney and Jon Killinger
Class: CS 415
Assignment: Project 3
Description: This project implements the FFT algorithm
"""
import numpy
import math
import cmath
def checkLength(arrayA, arrayB):
    """
    Checks length of both polynomial arrays, if the same they
    return original arrays.  Otherwise, 0s are appened to the
    smaller array
    """
    if(len(arrayA) == len(arrayB)):
        print("Same")
        return (arrayA, arrayB)
    elif(len(arrayA) > len(arrayB)):
        print("A > B")
        arrayB = appendZeros(arrayB, len(arrayA) - len(arrayB))
    else:
        print("B>A")
        arrayA = appendZeros(arrayA, len(arrayB) - len(arrayA))
    return (arrayA, arrayB)

def appendZeros(array2append, n):
    # Appends n number of zeros to an array
    for i in range(0, n):
        array2append.append(0)
    return array2append


def splitArray(array2split):
    """
    Splits an array into two equal parts one containing all of the
    values at odd indexs and the other at even indexes
    """
    oddArray = []
    evenArray = []
    for i in range(len(array2split)):
        if(i % 2 == 0):
            evenArray.append(array2split[i])
        else:
            oddArray.append(array2split[i])
    return (evenArray, oddArray)

def FFT (a, w):
    """
    Input: An array and root of unity
    Output: FFT of the array
    Description: This function will take in an array.  It will split the array into two
    different array based on whether the index is even or odd.  It will then perform FFT
    on both of these new arrays and put it back together.
    """
    if w == 1:
        return a
    (evenArray,oddArray) = splitArray(a)
    s = FFT(evenArray, pow(w, 2))
    sPrime = FFT(oddArray, pow(w,2))
    for j in range (len(n)/2-1):
        r[j] = s[j]+ pow(w, j) * sPrime[j]
        r[j+n/2] = s[j] - pow(w, j) * sPrime[j]
    return r

def componentMult (array1, array2):
    """
    Input: Two arrays
    Output: One array
    Description: This will multiply each element of the two arrays together.  For example
    it will multiply array1[0] and array2[0] together and then array[1] and array2[1] together
    and place them in a third array at their respective index
    """
    (array1, array2) = checkLength(array1, array2)
    componentArray = []
    for i in range (0, len(array1)):
        
        componentArray.append(array1[i] * array2[i])
   
    return componentArray

def inverseFFT(array2flip):
    """
    Input: One array
    Out: Inversed array
    Description: This function will first check to see if the length of the array is 0,
    if it is this function will return an empty array.  After this it will flip all of the elements in 
    the array besides the first element and divide them by the size of the array.
    """
    if(len(array2flip) == 0):
        return []
    size = len(array2flip)
    high = size -1
    mid = size / 2
    array2flip[0] = array2flip[0]/size
    for i in range(1, mid):
        array2flip[i] = array2flip[i]/size
        array2flip[high] = array2flip[high]/size
        array2flip[high], array2flip[i] = array2flip[i], array2flip[high]
        high -= 1
        
    return array2flip


def main():
    w = math.cos((2*math.pi)/2)
    m = math.sin((2*math.pi)/2) * 1j
    print(w, m)
    p = w + m
    print (p)

    z = cmath.exp((2*math.pi*1j)/2)
    print(z.real)
    a=  [float(1), float(-2), float(1), float(5)]
    print(inverseFFT(a))
    a = [1, 2, 3, 5]
    b = [1, 2,4,2,1,1,1,1]
    c = checkLength(a,b)
    d = [1, 2,3,4,5]
    f = [1,2,3,4,5, 5]
    print(c)
    (evenArray, oddArray) = splitArray(d)
    print("Evenarray: ", evenArray, "Odd array:",  oddArray)
    print(componentMult(f, d))
    """
    To DO:
    Figure out what n is in the case of w^n for fft
    test FFT function

    """
    

main()
