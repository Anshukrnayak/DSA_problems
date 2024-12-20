

# pair sum problem of the array : 
import numpy as np


def pair_sum(arr,k):

    count=0
    j=len(arr)-1
    i=0

    while i<=j:
        print(f' {arr[i]},{arr[j]} ')

        if arr[i]+arr[j]==k:
            
            count+=1
            i+=1
            j-=1
          
        if arr[i]+arr[j]<k:
            i+=1
        
        
        if arr[i]+arr[j]>k:
            j-=1
    
    return count

# time complexity of the program will be O(n)

def pair_sum(arr,k,i,j,count=0):

    print('recursive function execution ')

    if i>j: return count

    if arr[i]+arr[j]==k: return pair_sum(arr,k,i+1,j-1,count+1)

    elif arr[i]+arr[j]>k: return pair_sum(arr,k,i,j-1,count)

    elif arr[i]+arr[j]<k: return pair_sum(arr,k,i+1,j,count)



def main():
    print('This pair sum problem : ')
    arr=np.array([4,3,5,2,1])
    arr.sort()
    print(arr)

    count=pair_sum(arr,7,0,len(arr)-1)
    
    print(f'The pair sum of the program : {count} ')

if __name__=='__main__': main()

