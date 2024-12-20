

# reverse an integer : 

def reverse_integer(n):
    ans=0
    while n!=0:
        ans=ans*10+n%10
        n=n//10
    
    return ans
    

# Reverse an interger using recursion method 

def reverse_interger(n,ans=0):

    if n==0: return ans

    ans=ans*10+n%10

    return reverse_interger(n//10,ans)


def main():
    n=int(input('Enter a interger : '))
    ans=reverse_interger(n)
    print(f'Reverse interger : {ans} ')

if __name__=='__main__': main()

