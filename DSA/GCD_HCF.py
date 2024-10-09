
def GCD(a,b):
    
    if a%b==0: return b
    
    if b%a==0: return a
    
    if a>b:
        return GCD(a-b,b)
    else:
        return GCD(a,b-a)

def main():
    ans=GCD(25,15)
    print(ans)

if __name__=='__main__': main()

