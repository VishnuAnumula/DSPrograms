# Printing twin primes upto a specific value.
t=0
t1=0
a=int(input('enter a specific value upto where the twin primes should be printed'))
for v in range(2,a) :
    t=0
    t1=0
    for i in range(2,v) :
        if v%i==0 :
            t=1
    v2=v+2    
    for i1 in range(2,v2) :
        if v2%i1==0 :
            t1=1
    if t==0 and t1==0 :
        print(v,'and',v2)       
