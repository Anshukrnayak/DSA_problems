

def generate_prime_number_list(n): return [i for i in range(n)]

def geneator_number(n):
     for i in range(n+1): yield i

def main(): 
    n=int(input('Enter a number : '))

    my_list=geneator_number(n)
    print(sum(my_list))    

if __name__=='__main__': main()
