 


def sum_even(n):
    sum=0

    for i in range(0,n+1):
        if i%2==0:
            sum+=i 
    
    return sum


def sum_odd(n):
    sum=0
    for i in range(0,n+1):
        if i%2!=0:
            sum+=i 
            
    return sum 


def main():
    n=int(input('Enter a number : '))
    even=sum_even(n)
    odd=sum_odd(n)

    print(f'The sum of even numbers : {even} ')
    print(f'The sum of odd number : {odd} ')

if __name__=='__main__': main()

