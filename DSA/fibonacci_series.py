

def fibonacci_series(n):

    first_number=0
    second_number=1

    while first_number<=n:
        next_number=first_number+second_number
        print(next_number)
        first_number=second_number
        second_number=next_number 

        next_number+=1
    

def fib(n):

    if n==0 or n==1: return 1

    return fib(n-1)+fib(n-2)


def main():

    n=int(input('Enter an integer : '))
    ans=fib(n)



    print(f'The nth term : {ans} ')


if __name__=='__main__': main()

