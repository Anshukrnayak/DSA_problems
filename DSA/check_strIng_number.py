


def check_string_number(str):

    for i in range(0,len(str)):
        if not  str[i].isdigit(): return True
    
    return False


def main():
    str='dkdfkjds574734'

    ans=check_string_number(str)

    print(f'is a string : {ans} ')



if __name__=='__main__': main()