

def merger_sort_two(left,right):

    i=j=0
    arr=[]

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            arr.append(left[i])
            i+=1

        else: 
            arr.append(right[j])
            j+=1


    while i<len(left):
        arr.append(left[i])
        i+=1
    
    while j<len(right):
        arr.append(right[j])
        j+=1


    return arr


def merger_sort(arr):
    
    if len(arr)==1: return arr

    mid=len(arr)//2

    left_arr=arr[0:mid]
    right_arr=arr[mid:]

    left=merger_sort(left_arr)
    right=merger_sort(right_arr)

    return merger_sort_two(left,right)


def main():

    arr=[5,3,4,2,1,7]

    new_arr=merger_sort(arr)

    print(f'new sorted array : {new_arr} ')


if __name__=='__main__': main()

