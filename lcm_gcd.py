# Finding GCD and LCM.

a = int(input('Enter the first number'))
v = int(input('Enter the second number'))
highest=max(a,v)
while(True) :
    if highest%a==0 and highest%v==0 :
        lcm=highest
        break
    highest+=1
print('The LCM of',a,'and',v,'is',lcm)    
gcd=(a*v)//lcm
print('The GCD of',a,'and',v,'is',gcd)
