""""
Author: Sean Moloney and Jon Killinger

"""
import numpy
import math
import cmath
def checkLength(arrayA, arrayB):
# Checks length of both polynomial arrays, if the same they
# return original arrays.  Otherwise, 0s are appened to the
# smaller array
    if(len(arrayA) == len(arrayB)):
        return (arrayA, arrayB)
    elif(len(arrayA) > len(arrayB)):
        arrayB = appendZeros(arrayB, len(arrayA) - len(arrayB))
    else:
        arrayA = appendZeros(arrayA, len(arrayB) - len(arrayA))
    return (arrayA, arrayB)

def appendZeros(array2append, n):
# Appends n number of zeros to an array
    for i in range(0, n-1):
        array2append[i].append(0)
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
    componentArray = []
    for i in range (len(array1)):
        componentArray[i] = array1[i] * array2[i]

    return componentArray

def inverseFFT(array2flip):
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

main()
