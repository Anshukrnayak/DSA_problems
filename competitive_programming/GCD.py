
def GCD(a,b):
    if a==0: return b
    if b==0: return a

    if a>b: return GCD(a%b,b)
    else: return GCD(a,b%a)

def LCM(a,b): return (a*b)//GCD(a,b)

print(LCM(48,18))


