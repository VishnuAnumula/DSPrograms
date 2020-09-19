# Accept a number and print the count of digits in it without using for loop

v = int(input('Enter the first number'))
#print (v,'has',len(v),'digits')
s=0
n=v
while(v>0):
    r=v%10
    s=s+r
    v=v//10
print ('sum of the digits of',n,'is',s)