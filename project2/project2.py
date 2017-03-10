def primality3(n, k):
    a = True
    b = True
    c = True
    for i in range(0, 2):
        a = div_check(n, 2)
        b = div_check(n, 5)
        c = div_check(n, 7)
        if a == False or b == False or c == False:
            return False
            
    return primality2(n,k)

def primality2(n, k):
    a = ['1']
    m = mod(dec2bin(1), n)
    for i in range(k):
        primeCheck = expo(a, sub(n, ['1']))
        
        if(primeCheck != m):
            return False
        a = add(a, ['1'])
    return True
    


def div_check(n, a):
    (q, r) = div(n, dec2bin(a))
    if r != 0:
        return False
    else:
        return True
