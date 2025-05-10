
import math
def is_prime(x):
   if x<2:
      return False

   for num in range(2,math.sqrt(x)):
      if x%num==0:
         return False

   return True


if __name__=='__main__':
   try:
      x=int(input('Enter a number : '))
      if is_prime(x):
         print(f' x is a prime number : {x}')
      else:
         print(f'x is not a prime number : {x}')
   except:
      print('please insert a number : ')


