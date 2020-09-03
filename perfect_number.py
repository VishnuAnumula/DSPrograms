# Finding given number perfect or not.

a = int(input('Enter a number'))
sum=0
i=1
while(i<a) :
    if a%i==0 :
        sum=sum+i
    i=i+1
if sum==a :
    print(a,'is a perfect number')      
else :
    print(a,'is not a perfect number')       
