# Exception handling

# WAP to accept a number and print the sum of individual digits.
# I/p test cases
# 1.integer

x=input('enter a number to find sum of its digits: ')
try:
    n=int(x)
    print('The given value is an integer')
    s=0
    while n!=0:
        r=n%10
        n//=10
        s+=r
    print('The sum of digits of given no. is',s)
except:
    try:
        n=float(x)
        print('The given value is a float')
        s=0
        while n!=0:
            r=n%10
            n//=10
            s+=r
        print('The sum of digits of given no. is',s)
    except Exception as e:
        print('The given value is a string. ',type(e).__name__)