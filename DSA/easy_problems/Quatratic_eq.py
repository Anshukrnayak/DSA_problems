import math

def alpha(d,a,b):
    
    x=(-b+math.sqrt(d))/2*a

    return x

def beta(d,a,b):
    x=(-b-math.sqrt(d))/2*a

    return x


def is_imagenaray(a,b,c):
    d=pow(b,2)-4*a*c


    if d<0:
        print('D Imagenary number : ')
        return d 

    alp=alpha(d,a,b)
    bt=beta(d,a,b)

    return alp,bt 


def main():
    a=1
    b=5
    c=6   

    ans=is_imagenaray(a,b,c)

    print(ans)


if __name__=='__main__': main()
