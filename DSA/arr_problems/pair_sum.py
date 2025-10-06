
import numpy as np 

def pair_sum(arr,k):
    
    count=0

    for i in range(0,len(arr)):
        j=i+1
        while j<len(arr):
            if arr[i]+arr[j]==k: count+=1   

            j+=1

    return count

# Time complexity of the program will be o(n^2)


def pair_sum(arr,k,index=0,count=0):

    print(f'time complexity of the program will be o(n^2)')
    if index>=len(arr)-1: return count

    j=index+1
    while j<len(arr):
        if arr[index]+arr[j]==k: return pair_sum(arr,k,index+1,count+1)
        j+=1
    
    return pair_sum(arr,index+1,k,count)

# Time complexity of the program will be o(n^2)


def main():
    arr=np.array([3,5,2,1,4])

    count=pair_sum(arr,7)
    print(f'pair count : {count} ')


if __name__=='__main__': main()

