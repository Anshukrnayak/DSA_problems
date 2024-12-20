from typing import List

def add(a:int,b:int,arr:List[int]=[]):
    sum=a+b
    return arr.append(sum)


def main():
    a=10
    b=10
    ans=add(a,b)
    print(f' sum of {a} and {b} : {ans}')

if __name__=='__main__': main()


