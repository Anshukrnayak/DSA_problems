

def binary_search(arr,key):
    s=0
    e=len(arr)-1
    mid=s+(e-s)//2 

    while s<=e:
        if arr[mid]==key: return mid  

        if arr[mid]<key: s=mid+1

        else : e=mid-1 

        mid=s+(e-s)//2 
    
    return -1 


def binary_search(arr,key,s,e):
    
    mid=s+(e-s)//2 

    if arr[mid]==key: return mid 

    if arr[mid]<key: return binary_search(arr,key,mid+1,e)

    else: return binary_search(arr,key,s,mid-1)

    

def main():

    arr=[1,2,3,4,5,6,7,8,9,10]
    s=0
    e=len(arr)-1 

    index=binary_search(arr,2,s,e)

    print(index)



if __name__=='__main__': main()
