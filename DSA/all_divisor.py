
def Divisor(n,index=2):
    if index==n: return
    
    if n%index==0: print(index)
    
    Divisor(n,index+1)

def Prime_number(n,index=2):

    if index==n: return True
    
    if n%index==0: return False
    
    return Prime_number(n,index+1)


def main():
    
    ans=Prime_number(13)
    print(ans)    
        
if __name__=='__main__': main()

