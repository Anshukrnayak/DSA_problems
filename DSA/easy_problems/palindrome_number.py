
def reverse_integer(n,ans=0):
    if n==0: return ans

    ans=ans*10+n%10

    return reverse_integer(n//10,ans)


def palindrome_number(n):
    
    if reverse_integer(n)==n: return True

    return False



def main():
    n=int(input('Enter an integer : '))

    print(f'is {n} palindrome : {palindrome_number(n)} ') 


if __name__=='__main__': main()