

# Iteration way 
def linear_search(arr,key):

    for i in range(0,len(arr)):
        if arr[i]==key:
            return i 
    
    return -1 


# Recursive way 
def linear_search(arr,key,index=0):

    if index>=len(arr)-1: return -1

    if arr[index]==key: return index
    
    return linear_search(arr,key,index+1)



def main():
    arr=[1,2,3,5,4,6]
    index=linear_search(arr,4)
    print(f'index : {index} ')


if __name__=='__main__': main()