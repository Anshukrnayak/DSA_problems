

def sqrt_n(n):
    s=ans=0
    e=n
    mid=s+(e-s)//2 

    while s<=e:

        if mid*mid==n: return mid 

        if mid*mid>n: e=mid

        else :
            ans=mid 
            s=mid-1

        mid=s+(e-s)//2

    return ans     



# recursive way to solve this problem : 


def sqrt_n_recursion(n,e,s=0,ans=0):
    
    if s>=e: return ans 

    mid=s+(e-s)//2 

    if mid*mid==n: return mid 

    if mid*mid>n: return sqrt_n_recursion(n,mid,s,ans)

    else: 
        ans=mid 
        return sqrt_n_recursion(n,e,mid-1,ans)


def main():
    n=int(input('Enter an integer : '))
    e=n
    ans=sqrt_n(n,e)
    print(f'squre root of n is : {ans} ')
 
if __name__=='__main__': main()