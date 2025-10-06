
# even number comprehension
def even_number(n):
    return [x for x in range(0,n) if x%2==0]


def odd_number(n):
    return [x for x in range(0,n) if x%2!=0]


n=int(input('Enter a number : '))
even_arr=even_number(n)
odd_arr=even_number(n)

print(f'list of odd number : {odd_arr} ')

