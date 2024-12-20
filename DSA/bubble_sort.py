

import numpy as np 

def bubble_sort(arr):
    
    for i in range(0,len(arr)-1):
        j=0
        while j<len(arr)-1:
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
            
            j+=1
    
    


def main():
    arr=np.array([3,4,2,1,5])

    bubble_sort(arr)
    print(arr)



if __name__=='__main__': main()
