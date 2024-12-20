

def prime_number(n):

    for i in range(2,n):
        if n%i==0: return False 
    
    return True



def prime_number(n,index=2):

    if index==n-1: return True

    if n%index==0: return False 

    return prime_number(n,index+1)



def main():
    n=int(input('Enter a number : '))

    ans=prime_number(n)
    print(f'Is a prime number : {ans} ')



if __name__=='__main__': main()