import numpy as np

def sum(arr):
    sum=0
    for i in arr:
        sum+=i
    
    return sum

def main():
    arr=np.arange(1,101)
    ans=sum(arr)
    print(ans)
    

if __name__=='__main__': main()
