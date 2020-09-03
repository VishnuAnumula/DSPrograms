# Printing prime numbers upto a specific limit

a=int(input('enter a specific value upto where the prime numbers should be printed'))
print('prime numbers upto',a,'are')
for v in range(2,a) :
    t=0
    for i in range(2,v) :
        if v%i==0 :
            t=1
    if t==0 :
        print(v,' ')       
