
# Iteratite way to sum 
def sum_array(arr):

    sum=0 
    for index in arr:sum+=index
    
    return sum

# Recursive way to implement sum of array :

def sum_array(arr,index=0,sum=0):

    if index>=len(arr): return sum

    sum+=arr[index]

    return sum_array(arr,index+1,sum)

def main():
    arr=[3,4,5,2,1]
    sum=sum_array(arr)

    print(sum)

if __name__=='__main__': main()


