import numpy as np

def recursion_call(n):
    if n==0: return 
    
    print(f'Hello world {n}')
    recursion_call(n-1)
    print(f'Hello world {n} ')

def reverse_list(arr,s,e):
    if s>e: return 
    
    arr[s],arr[e]=arr[e],arr[s] 
    s+=1
    e-=1
    
    reverse_list(arr,s,e)


def palindrome_string(str,s,e):
    if s>=e: return True
    
    if str[s]==str[e]:return palindrome_string(str,s+1,e-1)
    
    else: return False 


def main():
    arr=np.array([1,2,3,4,5])
    str='pop'
    ans=palindrome_string(str,0,len(str)-1)
    print(ans)
    
    
if __name__=='__main__': main()

