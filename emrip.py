
## EMRIP Number or not

def reverse(n):
    num=n
    rev=0
    while n>0:
        rem=n%10
        rev=rev*10+rem
        n=n//10
    return rev

def isPallindrome(n):
    if n==reverse(n):
        return True
    else:
        return False

def isPrime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
            return True
    else:
        return False


def isEMRIP(n):
    if not isPallindrome(n):
        if isPrime(n):
            if isPrime(reverse(n)):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def EMRIPNumbers(ll,ul):
    for i in range(ll,ul+1):
        if isEMRIP(i):
            print(i)
EMRIPNumbers(10,100)