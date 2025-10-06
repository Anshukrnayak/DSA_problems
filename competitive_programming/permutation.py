
def factorial(n):
    if n==0 or n==1: return 1
    ans=1
    for i in range(2,n+1):ans*=i
    return ans


def combination(n,r):
    return (factorial(n))//(factorial(r)*factorial(n-r))



def fn(n):
    if n==0 or n==1:
        return 1
    return n*fn(n-1)

def permutation(n,r):
    return fn(n)//fn(n-r)

def combination_second(n,r):
    return permutation(n,r)//fn(r)

print(combination(10,3))


def fast_factorial(n,r,mod):
    return combination(n,r)%mod

print(permutation(10,3))

