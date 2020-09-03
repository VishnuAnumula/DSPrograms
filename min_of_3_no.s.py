# Finding minimum of three numbers.

a = int(input('Enter the first number'))
v = int(input('Enter the second number'))
v2 = int(input('Enter the third number'))
if a<v :
    if a<v2 :
        print(a,'is the least value among the three numbers')
    else :
        print(v2,'is the least value among the three numbers')    
else :
    if v<v2 :
        print(v,'is the least value among the three numbers')      
    else :
        print(v2,'is the least value among the three numbers')   
print(max(a,v,v2),'is the highest value among the three numbers')           