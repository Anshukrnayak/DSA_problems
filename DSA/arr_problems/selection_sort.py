

def selection_sort(arr):

    for i in range(0,len(arr)):
        j=i+1

        while j<len(arr):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]

            j+=1

def selection_sort(arr,index=0):
    if index>len(arr)-1: return 

    j=index+1

    while j<len(arr):
        if arr[index]>arr[j]:
            arr[index],arr[j]=arr[j],arr[index]
        j+=1

    selection_sort(arr,index+1)


# Time complexit  (n^2)
# Space complextiy (1)


def main():
    arr=[3,4,2,1,0]

    selection_sort(arr)
    print(arr)



if __name__=='__main__': main()