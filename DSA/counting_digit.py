
def counting_digit(number):
    count=0
    while number!=0:
	    count+=1
	    number=number//10
    
    return count

def counting_digit_rec(number,count=0):
    if number==0: return count
    
    return  counting_digit_rec(number//10,count+1)


def main():
    ans=counting_digit_rec(155553)
    print(ans)
    
if __name__=='__main__': main()
