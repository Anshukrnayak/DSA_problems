
def Amstrong_number(n):
    ans=0
    
    while n!=0:
        digit=n%10
        ans+=pow(digit,3)
        n=n//10
    
    return ans
# Recursion 
def Amstrong_number_rec(n,ans=0):
    if n==0: return ans
    
    ans+=pow(n%10,3)
    
    return Amstrong_number_rec(n//10,ans)
    
    
def Amstrong(n):

    if Amstrong_number_rec(n)==n: print('It is  Am_strong number')
    
    else: print('It is not Am_strong number ')
    
def main():
    
    Amstrong(153)
    

if __name__=='__main__': main()

