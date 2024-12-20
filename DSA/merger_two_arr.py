
import numpy as np 


def merger_two_arr(arr1,arr2):

    i=0
    j=0

    arr=[]

    while i<len(arr1) and j<len(arr2):
        
        if arr1[i]<arr2[j]:
             arr.append(arr1[i])
             i+=1
        
        else:
            arr.append(arr2[j])
            j+=1



    while i<len(arr1):
        arr.append(arr1[i])
        i+=1
    
    while j<len(arr2):
        arr.append(arr2[j])
        j+=1
    

    return arr


def merger_two_arr(arr1,arr2,i=0,j=0,arr=[]):

    if i>=len(arr1)-1 and j>=len(arr2)-1: return arr


    if i==len(arr1): arr.append(arr1[i])

    if j==len(arr2): arr.append(arr2[j])

    if arr1[i]<arr2[j]: 
        arr.append(arr1[i])
        return merger_two_arr(arr1,arr2,i+1,j,arr)
    else:
        arr.append(arr2[j])
        return merger_two_arr(arr1,arr2,i,j+1,arr)
    
    

# time complexity of the merger two array problem is O(n).

def main():
    arr1=[2,4,6,8,10]
    arr2=[1,3,5,7,9]
    
    arr=merger_two_arr(arr1,arr2)

    print(arr)


if __name__=='__main__': main()

