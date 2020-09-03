# Finding sum of digits of a number and checking whether it is armstrong number or not.

a=int(input('enter a number'))
org_a=a
sum=0
arm_sum=0
while(a!=0) :
    r=a%10
    sum+=r
    arm_sum+=r*r*r
    a//=10
print('sum of the digits of',org_a,'is',sum)
if arm_sum==org_a :
    print(org_a,'is a armstrong number')
else :
    print(org_a,'is not a armstrong number')
