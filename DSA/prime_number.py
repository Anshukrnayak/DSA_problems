
import numpy as np

def Prime_number(n):
    
    for i in range(2,n):
        if n%i==0: return False
    
    return True

# First  Approach 
def prime_series(series):
    
    prime_num_series=[]
 
    for item in series:
        if Prime_number(item): prime_num_series.append(1)
        else: prime_num_series.append(0)
           
    return prime_num_series

# Second Approach 

def prime_number_series(series):
    prime_num_series=[]
    
    for item in series:
        if Prime_number(item):
             prime_num_series.append(1)
             j=item*item
             
             while j<len(series):
                    prime_num_series.append(0)  
                    j=j+1
        
    return prime_num_series

def prime_number_count(series):
    prime_num_series=[]
    
    for item in series:
        if Prime_number(item):
             prime_num_series.append(1)
             j=item*item
             
             while j<len(series):
                    prime_num_series.append(0)  
                    j=j+1
                    
    count=0
    for item in prime_num_series:
            if item!=0: count+=1
        
    return count
    

def main():
    
    series=np.arange(1,10)
    prime_numbers=prime_number_count(series)
    
    print(prime_numbers)
    
    
    
if __name__=='__main__': main()

