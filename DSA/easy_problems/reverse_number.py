
def reverse_number(n):
    ans=0
    while n!=0:
        ans=ans*10+n%10
        n=n//10
    
    return ans

# recursive solution 
def reverse_number_rec(n,ans=0):
    
    if n==0: return ans
    
    ans=ans*10+n%10
    
    return reverse_number(n//10,ans)



def palindrome(n):
    print(reverse_number(n),n)
    if reverse_number(n)==n: return True
    
    else: return False
    

def main():
    ans=palindrome(121)
    print(f'Reverse of n : {ans} ')

if __name__=='__main__': main()

