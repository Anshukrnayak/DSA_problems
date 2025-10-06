
import numpy as np 
def palindrome_array(arr):

    s=0
    e=len(arr)-1

    while s<=e:
        if arr[s]==arr[e]:
            s+=1
            e-=1
        else: return False
    
    return True

def palindrome_array(arr,s,e):

    if s>=e: return True

    if arr[s]==arr[e]: return palindrome_array(arr,s+1,e-1)

    else: return False

    

def main():

    arr=np.array([1,2,3,2,1])

    ans=palindrome_array(arr,0,len(arr)-1)
    
    print(f'Is palindrome : {ans} ')


if __name__=='__main__': main()

