

def amstrong_number(n,ans=0):
    if n==0: return ans 

    ans+=pow(n%10,3)

    return amstrong_number(n//10,ans)


def amstrong(n):
    
    if amstrong_number(n)==n: return True

    return False


def main():

    n=int(input('Enter a number : '))
    
    print(f'Is amstrong {amstrong(n)} ')



if __name__=='__main__': main()

