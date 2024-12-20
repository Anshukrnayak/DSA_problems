
# first topic is decorators 

import time 

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time=time.time()
        result=func(*args,**kwargs)
        end_time=time.time()
        print(f': took time : {int(end_time-start_time)} second to execute this fuction  ')

        return result
    
    return wrapper


@time_decorator
def calculate_sum(n):
    print(sum(range(n+1)))
    

def main():

    n=int(input('Enter a number : '))
    calculate_sum(n)
    

if __name__=='__main__': main()